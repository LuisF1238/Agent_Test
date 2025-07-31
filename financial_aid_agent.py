from typing import Dict, Any, List
from agents import Agent
from datetime import datetime

class FinancialAidAgent:
    """Specialized agent for UC/CSU transfer financial aid guidance"""
    
    def __init__(self):
        self.agent = Agent(
            name="Financial Aid Specialist",
            instructions="""You are a specialized Financial Aid Counselor for UC/CSU transfer students. Your expertise includes:

CORE RESPONSIBILITIES:
- FAFSA guidance and deadlines
- Cal Grant applications and requirements  
- UC/CSU specific scholarships and grants
- Transfer student financial aid timelines
- Cost comparison between UC and CSU systems
- Work-study and student employment opportunities
- Loan options and debt management strategies

KNOWLEDGE BASE:
- Current UC tuition: ~$14,000/year (residents), ~$44,000/year (non-residents)
- Current CSU tuition: ~$6,000/year (residents), ~$18,000/year (non-residents)
- Cal Grant deadlines, eligibility requirements
- Priority FAFSA deadlines for UC/CSU
- Transfer-specific scholarship opportunities

APPROACH:
- Always ask about residency status and family income range
- Provide specific deadlines and action items
- Explain both need-based and merit-based options
- Address transfer student unique financial challenges
- Connect financial planning to transfer timeline

Stay focused on financial aid for UC/CSU transfer students only.""",
            model="4.1-nano",
            tools=[]
        )
        
        # Financial aid knowledge base
        self.financial_data = {
            'uc_costs': {
                'tuition_resident': 14436,
                'tuition_nonresident': 44196,
                'housing_avg': 15000,
                'books_supplies': 1200
            },
            'csu_costs': {
                'tuition_resident': 5982,
                'tuition_nonresident': 17622,
                'housing_avg': 12000,
                'books_supplies': 1000
            },
            'deadlines': {
                'fafsa_priority': 'March 2',
                'cal_grant': 'March 2',
                'uc_app_deadline': 'Nov 30',
                'csu_app_deadline': 'Nov 30'
            }
        }
    
    def handle_query(self, query: str, student_context: Dict[str, Any] = None) -> str:
        """Process financial aid related queries"""
        query_lower = query.lower()
        
        # Initialize context if not provided
        if student_context is None:
            student_context = {}
        
        # Route to specific financial aid topic
        if any(word in query_lower for word in ['fafsa', 'federal aid']):
            return self._handle_fafsa_query(query, student_context)
        elif any(word in query_lower for word in ['cal grant', 'california grant']):
            return self._handle_calgrant_query(query, student_context)
        elif any(word in query_lower for word in ['cost', 'tuition', 'expensive']):
            return self._handle_cost_query(query, student_context)
        elif any(word in query_lower for word in ['scholarship', 'merit']):
            return self._handle_scholarship_query(query, student_context)
        elif any(word in query_lower for word in ['deadline', 'when', 'timeline']):
            return self._handle_deadline_query(query, student_context)
        else:
            return self._handle_general_financial_query(query, student_context)
    
    def _handle_fafsa_query(self, query: str, context: Dict[str, Any]) -> str:
        current_year = datetime.now().year
        return f"""**FAFSA Guidance for UC/CSU Transfer Students**

**Priority Deadline:** March 2, {current_year + 1} (for {current_year + 1}-{current_year + 2} academic year)

**Key Points for Transfer Students:**
- Complete FAFSA even if you think you won't qualify
- Use your (and parents' if dependent) {current_year - 1} tax information
- List all UC/CSU schools you're applying to (up to 10 schools)

**Transfer-Specific Tips:**
✓ Update your FAFSA once you know your transfer school
✅ Verify your enrolled units meet financial aid requirements
✓ Check if your community college credits affect your aid eligibility

**Next Steps:**
1. Gather required documents (SSN, tax returns, bank statements)
2. Create FSA ID at studentaid.gov
3. Complete FAFSA at fafsa.gov
4. Submit by March 2 for priority consideration

**Questions to consider:** Are you a California resident? What's your expected family contribution (EFC)?"""
    
    def _handle_calgrant_query(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Cal Grant Information for Transfer Students**

**Three Cal Grant Types:**
- **Cal Grant A:** Tuition/fees coverage (GPA 3.0+ required)
- **Cal Grant B:** Living allowance + tuition (low-income, GPA 2.0+)  
- **Cal Grant C:** Vocational/career training (limited for transfers)

**Transfer Student Requirements:**
✓ California resident for 1+ years
✓ Submit FAFSA and GPA Verification Form by March 2
✓ Meet income/asset limits
✓ Maintain academic progress

**GPA Requirements:**
- Community College GPA: 2.4+ (Cal Grant B) or 3.0+ (Cal Grant A)
- Must have GPA verified by your community college

**Coverage Amounts (2024-25):**
- UC System: Up to $14,436 (tuition) + $1,648 (access award)
- CSU System: Up to $5,982 (tuition) + $1,648 (access award)

**Action Items:**
1. Submit GPA Verification Form to your community college financial aid office
2. Complete FAFSA by March 2
3. Check eligibility at csac.ca.gov"""
    
    def _handle_cost_query(self, query: str, context: Dict[str, Any]) -> str:
        uc_total = self.financial_data['uc_costs']['tuition_resident'] + self.financial_data['uc_costs']['housing_avg']
        csu_total = self.financial_data['csu_costs']['tuition_resident'] + self.financial_data['csu_costs']['housing_avg']
        
        return f"""**UC vs CSU Cost Comparison (2024-25 Academic Year)**

**UC System (Resident):**
- Tuition & Fees: ${self.financial_data['uc_costs']['tuition_resident']:,}
- Housing & Meals: ${self.financial_data['uc_costs']['housing_avg']:,}
- Books & Supplies: ${self.financial_data['uc_costs']['books_supplies']:,}
- **Total Annual Cost: ~${uc_total + self.financial_data['uc_costs']['books_supplies']:,}**

**CSU System (Resident):**
- Tuition & Fees: ${self.financial_data['csu_costs']['tuition_resident']:,}
- Housing & Meals: ${self.financial_data['csu_costs']['housing_avg']:,}
- Books & Supplies: ${self.financial_data['csu_costs']['books_supplies']:,}
- **Total Annual Cost: ~${csu_total + self.financial_data['csu_costs']['books_supplies']:,}**

**Cost-Saving Strategies:**
💰 Apply for Cal Grant (covers most/all tuition)
🏠 Consider commuting or shared housing
📚 Use library resources, rent/buy used textbooks
💼 Work-study jobs (earn while studying)
🎓 Complete transfer in 2 years to minimize costs

**Financial Aid Can Cover:**
- With maximum aid, UC can cost as little as $8,000/year
- CSU can be nearly free with full Cal Grant + Pell Grant

Need help calculating your specific costs?"""
    
    def _handle_scholarship_query(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Scholarship Opportunities for Transfer Students**

**UC-Specific Scholarships:**
- UC Transfer Scholarship: $2,000-$5,000
- Blue and Gold Opportunity Plan: Covers tuition for families earning <$80,000
- Campus-specific scholarships (check individual UC websites)

**CSU-Specific Scholarships:**
- State University Grant: Need-based aid
- CSU Scholarship Plus: Merit-based awards
- EOP (Educational Opportunity Program) grants

**General Transfer Scholarships:**
- Jack Kent Cooke Foundation Transfer Scholarship: Up to $55,000
- Phi Theta Kappa Transfer Scholarships: $1,000-$30,000
- Hispanic Scholarship Fund, United Negro College Fund, Asian Pacific Fund

**Major-Specific Scholarships:**
- STEM: NSF scholarships, engineering society awards
- Business: Beta Alpha Psi, accounting firm scholarships
- Education: Future teacher programs, Teach Grant

**Application Tips:**
✓ Start searching early (junior year at community college)
✓ Apply broadly - even small scholarships add up
✓ Focus on your transfer story and goals
✓ Get strong letters of recommendation
✓ Meet all deadlines

**Resources:**
- Fastweb.com, Scholarships.com
- Your community college financial aid office
- Target UC/CSU financial aid websites

Which field of study are you planning to transfer into?"""
    
    def _handle_deadline_query(self, query: str, context: Dict[str, Any]) -> str:
        current_year = datetime.now().year
        return f"""**Critical Financial Aid Deadlines for Transfer Students**

**PRIORITY DEADLINES (Academic Year {current_year + 1}-{current_year + 2}):**

📅 **March 2, {current_year + 1}**
- FAFSA priority deadline
- Cal Grant application deadline
- GPA Verification Form due

📅 **November 30, {current_year}**
- UC application deadline
- CSU application deadline

📅 **January 31, {current_year + 1}**
- Final FAFSA deadline for Cal Grant consideration

**TRANSFER TIMELINE:**
- **Fall before transfer:** Complete applications, start financial aid research
- **Spring of transfer year:** Submit FAFSA/Cal Grant, apply for scholarships
- **Summer before transfer:** Accept aid packages, plan budget

**IMPORTANT NOTES:**
⚠️ Missing March 2 deadline means losing Cal Grant eligibility
⚠️ Some campus scholarships have earlier deadlines (check individual schools)
⚠️ Transfer students must update FAFSA with final school choice

**Monthly Action Items:**
- **October:** Research scholarships, gather financial documents
- **November:** Submit transfer applications
- **December-January:** Complete FAFSA
- **February:** Submit final documents, verify information
- **March-May:** Compare aid packages, make final decision

Don't wait - financial aid is first-come, first-served after priority deadlines!"""
    
    def _handle_general_financial_query(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Financial Aid Overview for UC/CSU Transfer Students**

**Available Aid Types:**
1. **Grants** (Free money - don't repay)
   - Federal Pell Grant: Up to $7,395/year
   - Cal Grant A/B: Covers tuition + living allowance
   - UC/CSU institutional grants

2. **Scholarships** (Merit-based, free money)
   - Transfer-specific scholarships
   - Major-specific awards
   - Private foundation scholarships

3. **Work-Study** (Earn while you learn)
   - On-campus jobs with flexible schedules
   - $12-$18/hour typically

4. **Student Loans** (Repayment required)
   - Federal Direct Loans: Better terms than private
   - Borrow only what you need

**Transfer Student Advantages:**
✓ Lower debt from community college start
✓ Mature approach to financial planning
✓ Eligible for junior/senior level opportunities
✓ Strong academic records from CC success

**Getting Started Checklist:**
□ Complete FAFSA by March 2
□ Submit Cal Grant GPA Verification Form  
□ Research transfer scholarships
□ Calculate total cost of attendance
□ Create a 2-year budget plan

**Key Resources:**
- Studentaid.gov (federal aid information)
- CSAC.ca.gov (California aid programs)
- Individual UC/CSU financial aid websites

What specific aspect of financial aid planning would you like to explore further?"""