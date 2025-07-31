#!/usr/bin/env python3
"""
Main entry point for the Transfer Counselor Agent System

A multi-agent system designed to help community college students 
transfer to UC and CSU schools with specialized agents for:
- Financial aid guidance
- Career counseling  
- Course difficulty management
- Transfer coordination
"""

from coordinator_agent import CoordinatorAgent
from financial_aid_agent import FinancialAidAgent
from career_counselor_agent import CareerCounselorAgent
from course_difficulty_agent import CourseDifficultyAgent

class TransferCounselorSystem:
    """Main system that orchestrates all transfer counseling agents"""
    
    def __init__(self):
        # Initialize coordinator agent
        self.coordinator = CoordinatorAgent()
        
        # Initialize specialized agents
        self.financial_aid_agent = FinancialAidAgent()
        self.career_counselor_agent = CareerCounselorAgent()
        self.course_difficulty_agent = CourseDifficultyAgent()
        
        # Register agents with coordinator
        self.coordinator.register_agent('financial_aid', self.financial_aid_agent)
        self.coordinator.register_agent('career_counselor', self.career_counselor_agent)  
        self.coordinator.register_agent('course_difficulty', self.course_difficulty_agent)
        
        print("🎓 Transfer Counselor System Initialized")
        print("Available assistance:")
        print("💰 Financial Aid - FAFSA, scholarships, cost planning")
        print("💼 Career Counseling - Major selection, career paths")
        print("📚 Academic Planning - Course difficulty, study strategies")
        print("🤖 Coordinator - Routes queries to appropriate specialists")
        print("-" * 60)
    
    def process_query(self, student_query: str, student_context: dict = None):
        """Process a student query through the appropriate agent(s)"""
        if student_context is None:
            student_context = {}
            
        # Route query through coordinator
        result = self.coordinator.route_query(student_query, student_context)
        
        return result
    
    def interactive_session(self):
        """Run interactive counseling session"""
        print("\n🌟 Welcome to your UC/CSU Transfer Counseling Session!")
        print("Ask me anything about transferring, financial aid, careers, or academics.")
        print("Type 'quit' to end the session.\n")
        
        student_context = {}
        
        while True:
            try:
                # Get user input
                query = input("\n📝 Your question: ").strip()
                
                if query.lower() in ['quit', 'exit', 'bye']:
                    print("\n🎯 Good luck with your transfer journey!")
                    print("Remember: You've got this! 💪")
                    break
                
                if not query:
                    print("Please enter a question about UC/CSU transfer, financial aid, careers, or academics.")
                    continue
                
                # Process query
                print("\n🤔 Processing your question...")
                result = self.process_query(query, student_context)
                
                # Display response
                print("\n" + "="*80)
                print(f"📍 Response from: {result['agent_used'].title().replace('_', ' ')}")
                print("="*80)
                print(result['response'])
                
                if result.get('agents_consulted'):
                    print(f"\n👥 Specialists consulted: {', '.join(result['agents_consulted'])}")
                
                print("\n" + "-"*60)
                
            except KeyboardInterrupt:
                print("\n\n🎯 Session ended. Good luck with your transfer goals!")
                break
            except Exception as e:
                print(f"\n❌ Error processing your question: {e}")
                print("Please try rephrasing your question.")

def main():
    """Main function to run the transfer counselor system"""
    system = TransferCounselorSystem()
    
    # Example usage
    print("\n📋 Example Questions You Can Ask:")
    print("• 'How do I apply for financial aid for UC schools?'")
    print("• 'What career paths are available with a psychology major?'")
    print("• 'How can I manage my course load while working part-time?'")
    print("• 'What's the difference between UC and CSU for business majors?'")
    print("• 'I'm struggling in organic chemistry, what should I do?'")
    
    # Start interactive session
    system.interactive_session()

if __name__ == "__main__":
    main()