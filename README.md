# Transfer Counselor Agent System

A comprehensive multi-agent system designed to help community college students successfully transfer to UC and CSU schools.

## 🎯 System Overview

This system provides specialized counseling through multiple AI agents with built-in guardrails to ensure responses stay focused on transfer and career-related topics.

### Key Components

- **🤖 Coordinator Agent**: Routes queries and manages multi-agent responses
- **💰 Financial Aid Agent**: FAFSA, scholarships, grants, cost planning
- **💼 Career Counselor Agent**: Major selection, career paths, job prospects
- **📚 Course Difficulty Agent**: Academic planning, study strategies, course management
- **🛡️ Guardrails System**: Ensures responses stay on-topic for transfer counseling

## 🚀 Quick Start

### Run Interactive Session
```bash
python main.py
```

### Use in Code
```python
from main import TransferCounselorSystem

system = TransferCounselorSystem()
result = system.process_query("How do I apply for financial aid?")
print(result['response'])
```

## 📋 Features

### Specialized Expertise
- **Financial Aid**: FAFSA deadlines, Cal Grant requirements, scholarship opportunities
- **Career Guidance**: Major selection, salary expectations, career paths
- **Academic Success**: Course planning, study strategies, GPA management
- **Transfer Planning**: UC vs CSU comparison, prerequisite tracking

### Built-in Safety
- Topic guardrails prevent off-topic discussions
- Focused on defensive/educational use only
- Redirects inappropriate queries to transfer-related topics

### Multi-Agent Coordination
- Single queries can consult multiple specialists
- Synthesized responses from relevant experts
- Context preservation across conversation

## 🎓 Example Queries

The system can handle questions like:
- "What financial aid is available for UC transfers?"
- "Which major should I choose for a career in tech?"
- "How do I manage a heavy course load while working?"
- "What's the difference between UC Berkeley and Cal Poly for engineering?"
- "I'm struggling in organic chemistry, what should I do?"

## 🏗️ Architecture

```
TransferCounselorSystem
├── CoordinatorAgent (main router)
├── FinancialAidAgent (specialized counselor)
├── CareerCounselorAgent (specialized counselor)
├── CourseDifficultyAgent (specialized counselor)
└── TransferGuardrails (safety system)
```

## 🛡️ Guardrails

The system includes comprehensive guardrails that:
- Allow transfer, career, financial aid, and academic topics
- Block off-topic discussions (entertainment, personal relationships, etc.)
- Provide helpful redirection messages
- Maintain focus on UC/CSU transfer goals

## 📁 File Structure

```
Agent_Test/
├── main.py                    # Main system entry point
├── coordinator_agent.py       # Master coordination logic
├── financial_aid_agent.py     # Financial aid expertise
├── career_counselor_agent.py  # Career guidance
├── course_difficulty_agent.py # Academic planning
├── guardrails.py             # Safety and topic filtering
├── model_config.py           # Agent configuration
└── README.md                 # This file
```

## 🎯 Use Cases

Perfect for:
- Community college transfer counseling
- Academic advising systems
- Career guidance platforms
- Financial aid assistance tools
- Educational chatbots with focused expertise

## 📊 Agent Specializations

### Financial Aid Agent
- FAFSA guidance and deadlines
- Cal Grant applications
- UC/CSU cost comparisons
- Scholarship opportunities
- Financial planning strategies

### Career Counselor Agent
- Major selection guidance
- Career path exploration
- Salary expectations
- Industry analysis
- Professional development

### Course Difficulty Agent
- Study strategies and techniques
- Course load management
- GPA improvement plans
- Time management
- Academic success skills

## 🔧 Customization

The system is designed to be easily customizable:
- Add new specialized agents
- Modify guardrails for different topics
- Extend knowledge bases
- Integrate with external APIs
- Customize response formatting

## 🤝 Contributing

This system prioritizes defensive security and educational use. Any modifications should maintain focus on helping students achieve their educational goals safely and effectively.