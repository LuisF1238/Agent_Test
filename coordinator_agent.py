from typing import Dict, Any, List
from guardrails import TransferGuardrails
from agents import Agent

class CoordinatorAgent:
    """Master coordinator agent that manages all specialized transfer counseling agents"""
    
    def __init__(self):
        self.guardrails = TransferGuardrails()
        self.specialized_agents = {}
        self.conversation_history = []
        
        # Initialize the coordinator agent
        self.agent = Agent(
            name="Transfer Coordinator",
            instructions="""You are the Master Transfer Coordinator responsible for:
            1. Routing student queries to appropriate specialized agents
            2. Ensuring all responses stay within transfer/career counseling scope
            3. Coordinating multi-agent responses when needed
            4. Maintaining conversation context across agents
            
            You work with:
            - Financial Aid Agent: Handles FAFSA, scholarships, grants, cost planning
            - Career Counselor Agent: Provides career guidance and major selection
            - Course Difficulty Agent: Helps with course planning and academic strategies
            
            Always prioritize student success in UC/CSU transfer goals.""",
            model="4.1-nano",
            tools=[]
        )
    
    def register_agent(self, agent_type: str, agent_instance):
        """Register a specialized agent with the coordinator"""
        self.specialized_agents[agent_type] = agent_instance
    
    def route_query(self, query: str, student_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Route student query to appropriate agent(s) based on content analysis"""
        
        # First, check guardrails
        guardrail_check = self.guardrails.is_query_allowed(query)
        if not guardrail_check['allowed']:
            return {
                'response': self.guardrails.get_redirect_message(guardrail_check['category']),
                'agent_used': 'coordinator',
                'status': 'blocked'
            }
        
        # Determine which agent(s) should handle the query
        category = guardrail_check['category']
        selected_agents = self._select_agents(category, query)
        
        # Route to appropriate agent(s)
        if len(selected_agents) == 1:
            return self._single_agent_response(selected_agents[0], query, student_context)
        elif len(selected_agents) > 1:
            return self._multi_agent_response(selected_agents, query, student_context)
        else:
            # Default to coordinator for general queries
            return self._coordinator_response(query, student_context)
    
    def _select_agents(self, category: str, query: str) -> List[str]:
        """Select appropriate agents based on query category and content"""
        query_lower = query.lower()
        selected = []
        
        # Financial aid keywords
        financial_keywords = ['financial', 'cost', 'tuition', 'scholarship', 'grant', 'fafsa', 'loan']
        if category == 'financial_aid' or any(keyword in query_lower for keyword in financial_keywords):
            selected.append('financial_aid')
        
        # Career counseling keywords
        career_keywords = ['career', 'major', 'job', 'profession', 'salary', 'internship']
        if category == 'career' or any(keyword in query_lower for keyword in career_keywords):
            selected.append('career_counselor')
        
        # Course difficulty keywords
        course_keywords = ['course', 'class', 'difficult', 'study', 'grade', 'academic']
        if category == 'academic' or any(keyword in query_lower for keyword in course_keywords):
            selected.append('course_difficulty')
        
        return selected
    
    def _single_agent_response(self, agent_type: str, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle response from a single specialized agent"""
        if agent_type in self.specialized_agents:
            agent = self.specialized_agents[agent_type]
            response = agent.handle_query(query, context)
            return {
                'response': response,
                'agent_used': agent_type,
                'status': 'success'
            }
        else:
            return self._coordinator_response(query, context)
    
    def _multi_agent_response(self, agent_types: List[str], query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate response from multiple agents"""
        responses = {}
        for agent_type in agent_types:
            if agent_type in self.specialized_agents:
                agent = self.specialized_agents[agent_type]
                responses[agent_type] = agent.handle_query(query, context)
        
        # Synthesize multi-agent response
        synthesized_response = self._synthesize_responses(responses, query)
        return {
            'response': synthesized_response,
            'agent_used': 'multi_agent',
            'agents_consulted': agent_types,
            'status': 'success'
        }
    
    def _coordinator_response(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general transfer coordination queries"""
        response = f"""I'm here to help you with your UC/CSU transfer journey! 

For your question about: "{query}"

I can connect you with our specialized counselors:
- 🎓 **Financial Aid Specialist** - FAFSA, scholarships, cost planning
- 💼 **Career Counselor** - Major selection, career paths, job prospects  
- 📚 **Academic Advisor** - Course planning, difficulty management, study strategies

What specific aspect would you like to explore further?"""
        
        return {
            'response': response,
            'agent_used': 'coordinator',
            'status': 'success'
        }
    
    def _synthesize_responses(self, responses: Dict[str, str], original_query: str) -> str:
        """Combine responses from multiple agents into coherent answer"""
        synthesized = f"Here's comprehensive guidance for your question:\n\n"
        
        agent_titles = {
            'financial_aid': '💰 Financial Aid Perspective',
            'career_counselor': '💼 Career Guidance',
            'course_difficulty': '📚 Academic Planning'
        }
        
        for agent_type, response in responses.items():
            title = agent_titles.get(agent_type, f'{agent_type.title()} Advice')
            synthesized += f"**{title}:**\n{response}\n\n"
        
        synthesized += "---\n*This comprehensive answer combines insights from our specialized transfer counseling team.*"
        return synthesized