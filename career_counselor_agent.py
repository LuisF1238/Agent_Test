from typing import Dict, Any, List
from agents import Agent

class CareerCounselorAgent:
    """Specialized agent for career counseling and major selection for UC/CSU transfer students"""
    
    def __init__(self):
        self.agent = Agent(
            name="Career Counselor",
            instructions="""You are a specialized Career Counselor for UC/CSU transfer students. Your expertise includes:

CORE RESPONSIBILITIES:
- Major selection based on career goals and interests
- UC vs CSU program comparison for specific majors
- Career outlook and job market analysis
- Salary expectations and growth potential
- Internship and networking strategies
- Professional development planning
- Transfer pathway optimization for career goals

KNOWLEDGE AREAS:
- Popular transfer majors and their requirements
- Industry trends and emerging fields
- Professional licensing requirements
- Graduate school preparation
- Career resources at UC/CSU campuses
- Alumni networks and career services

APPROACH:
- Assess student interests, values, and skills
- Connect academic choices to career outcomes
- Provide realistic timelines and expectations
- Encourage exploration while being practical
- Address transfer student unique advantages

Focus exclusively on career guidance for UC/CSU transfer students.""",
            model="4.1-nano",
            tools=[]
        )
        
        # Career data knowledge base
        self.career_data = {
            'popular_majors': {
                'business': {
                    'uc_programs': ['UC Berkeley Haas', 'UCLA Anderson', 'UC Irvine'],
                    'csu_programs': ['SDSU', 'Cal Poly SLO', 'CSU Long Beach'],
                    'career_paths': ['Management', 'Consulting', 'Finance', 'Marketing'],
                    'avg_salary': 65000,
                    'job_growth': 'Stable'
                },
                'computer_science': {
                    'uc_programs': ['UC Berkeley', 'UCLA', 'UC San Diego', 'UC Irvine'],
                    'csu_programs': ['Cal Poly SLO', 'SJSU', 'SDSU'],
                    'career_paths': ['Software Engineer', 'Data Scientist', 'Product Manager'],
                    'avg_salary': 95000,
                    'job_growth': 'High'
                },
                'psychology': {
                    'uc_programs': ['UCLA', 'UC Berkeley', 'UCSD'],
                    'csu_programs': ['SDSU', 'CSU Long Beach', 'SF State'],
                    'career_paths': ['Clinical Psychology', 'Counseling', 'Research', 'HR'],
                    'avg_salary': 55000,
                    'job_growth': 'Moderate',
                    'grad_school': 'Often required'
                },
                'engineering': {
                    'uc_programs': ['UC Berkeley', 'UCLA', 'UCSD', 'UC Irvine'],
                    'csu_programs': ['Cal Poly SLO', 'Cal Poly Pomona', 'SJSU'],
                    'career_paths': ['Design Engineer', 'Project Manager', 'Research'],
                    'avg_salary': 85000,
                    'job_growth': 'High'
                }
            },
            'career_resources': {
                'assessment_tools': ['O*NET Interest Profiler', 'Myers-Briggs', 'Strong Interest Inventory'],
                'networking': ['LinkedIn', 'Professional associations', 'Alumni networks'],
                'skill_building': ['Internships', 'Part-time work', 'Volunteer experience']
            }
        }
    
    def handle_query(self, query: str, student_context: Dict[str, Any] = None) -> str:
        """Process career counseling related queries"""
        query_lower = query.lower()
        
        if student_context is None:
            student_context = {}
        
        # Route to specific career counseling topic
        if any(word in query_lower for word in ['major', 'what should i study']):
            return self._handle_major_selection(query, student_context)
        elif any(word in query_lower for word in ['salary', 'pay', 'money', 'income']):
            return self._handle_salary_inquiry(query, student_context)
        elif any(word in query_lower for word in ['job', 'career path', 'employment']):
            return self._handle_career_paths(query, student_context)
        elif any(word in query_lower for word in ['internship', 'experience', 'networking']):
            return self._handle_experience_building(query, student_context)
        elif any(word in query_lower for word in ['uc vs csu', 'which school']):
            return self._handle_school_comparison(query, student_context)
        else:
            return self._handle_general_career_guidance(query, student_context)
    
    def _handle_major_selection(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Major Selection Guidance for Transfer Students**

**Self-Assessment Questions:**
🎯 What subjects do you genuinely enjoy studying?
💡 What problems do you want to help solve in the world?
⚡ What activities make you lose track of time?
💰 What lifestyle and income goals do you have?

**Popular Transfer-Friendly Majors:**

**High-Demand Fields:**
- **Computer Science/Engineering:** Strong job market, high salaries ($80k-$120k)
- **Business/Economics:** Versatile, good networking opportunities ($50k-$90k)
- **Healthcare (Nursing, Pre-med):** Stable, growing field ($60k-$100k+)
- **Data Science/Analytics:** Emerging field, high demand ($70k-$110k)

**Growing Fields:**
- **Environmental Science:** Sustainability focus, moderate growth
- **Digital Marketing:** Creative + analytical, flexible work options
- **Social Work/Public Policy:** Meaningful work, moderate pay
- **Education:** Stable, rewarding, summers off

**Major Selection Strategy:**
✓ Research prerequisite courses at your target UC/CSU
✓ Talk to professionals in fields of interest
✓ Consider double majors or minors
✓ Look at job placement rates from specific programs

**Resources:**
- O*NET Interest Profiler (free career assessment)
- Informational interviews with alumni
- Career center resources at your community college

**Questions for you:**
- What subjects are you currently excelling in?
- Do you prefer working with people, data, or creative projects?
- Are you open to graduate school, or prefer entering workforce after bachelor's?

What interests or strengths would you like to explore further?"""
    
    def _handle_salary_inquiry(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Salary Expectations for UC/CSU Graduates**

**Entry-Level Salaries by Major (California):**

**High-Paying Fields:**
- **Computer Science:** $85k-$120k (FAANG companies: $150k+)
- **Engineering:** $75k-$100k (varies by specialty)
- **Finance/Business:** $55k-$80k (investment banking: $100k+)
- **Data Science:** $80k-$110k

**Moderate-Paying Fields:**
- **Healthcare (RN):** $80k-$95k (high demand in CA)
- **Marketing:** $45k-$65k
- **Psychology:** $40k-$60k (higher with grad school)
- **Education:** $50k-$70k (plus benefits, tenure)

**UC vs CSU Salary Impact:**
- UC graduates average 10-15% higher starting salaries
- CSU graduates often have less student debt
- Long-term career success depends more on skills than school name

**Factors Affecting Salary:**
🌟 **Location:** Bay Area/LA vs Central Valley (20-40% difference)
🎓 **Experience:** Internships, projects, leadership roles
🏢 **Industry:** Tech, finance, healthcare pay premiums
📈 **Advanced degrees:** MBA, MS can increase earnings 30-50%

**Salary Growth Expectations:**
- Years 1-3: 5-10% annual increases typical
- Mid-career: $20k-$40k above starting salary
- Senior roles: $100k+ in most professional fields

**Financial Reality Check:**
- California cost of living is 30-50% above national average
- $70k in California ≈ $50k in most other states
- Consider total compensation (benefits, stock options, bonuses)

**Maximizing Earning Potential:**
✓ Build technical and leadership skills
✓ Network within your industry
✓ Consider certifications and continuing education
✓ Be open to job changes every 3-5 years

What specific field are you considering? I can provide more detailed salary information."""
    
    def _handle_career_paths(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Career Path Planning for Transfer Students**

**Advantages of Transfer Students:**
✓ Mature perspective and work ethic
✓ Lower debt burden from community college
✓ Clear focus on career goals
✓ Life experience and diverse backgrounds

**Career Development Timeline:**

**Junior Year (First year at UC/CSU):**
- Join professional clubs and organizations
- Attend career fairs and networking events
- Seek informational interviews
- Apply for summer internships
- Build LinkedIn profile

**Senior Year:**
- Complete capstone projects or thesis
- Leverage career services for job search
- Apply to jobs 6-9 months before graduation
- Consider graduate school applications
- Build professional references

**Popular Career Trajectories:**

**Business Track:**
Entry → Analyst → Manager → Director → VP/C-Suite
Timeline: 2-3 years per level

**Tech Track:**
Junior Developer → Developer → Senior Developer → Lead → Manager/Architect
Timeline: 1-2 years per level

**Healthcare Track:**
New Grad → Staff → Charge Nurse → Manager → Administrator
Timeline: 2-5 years per level

**Education Track:**
New Teacher → Veteran Teacher → Department Head → Administrator
Timeline: 3-7 years per level

**Career Pivoting Strategies:**
- Leverage transferable skills
- Consider adjacent industries
- Pursue additional certifications
- Network across different fields
- Use UC/CSU alumni networks

**Professional Development:**
🎯 **Technical Skills:** Stay current with industry trends
📈 **Leadership:** Take on project management roles
🤝 **Communication:** Practice public speaking, writing
🌐 **Networking:** Maintain professional relationships

**Job Search Resources:**
- UC/CSU career centers (lifetime access for alumni)
- LinkedIn job search and networking
- Industry-specific job boards
- Professional association career services
- Alumni mentorship programs

What specific career field interests you most? I can provide more targeted guidance."""
    
    def _handle_experience_building(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Building Professional Experience as a Transfer Student**

**Internship Strategy:**

**When to Start:** Begin searching junior year (first year at UC/CSU)
**Where to Look:**
- Campus career centers
- Company websites
- LinkedIn, Indeed, Glassdoor
- Professional association websites
- Faculty connections and research opportunities

**Types of Experience:**

**1. Formal Internships**
- Summer programs (10-12 weeks)
- Part-time during school year
- Virtual/remote opportunities
- Paid vs unpaid (aim for paid when possible)

**2. Research Opportunities**
- Work with professors on research projects
- Undergraduate research programs
- Independent study courses
- Research conferences and presentations

**3. Campus Involvement**
- Student government
- Professional clubs (relevant to your major)
- Peer tutoring or mentoring
- Campus newspaper, radio, organizations

**4. Community Engagement**
- Volunteer work related to career interests
- Nonprofit board service
- Community organizing
- Service learning courses

**Networking Strategies:**

**Professional Networking:**
🤝 Join relevant professional associations
📧 Conduct informational interviews (2-3 per month)
💼 Attend industry conferences and meetups
🎓 Connect with UC/CSU alumni in your field

**Digital Presence:**
- Optimize LinkedIn profile
- Create professional email signature
- Consider personal website/portfolio
- Engage thoughtfully on professional social media

**Making the Most of Limited Time:**
- Quality over quantity in activities
- Focus on leadership roles
- Document your achievements
- Ask for letters of recommendation early
- Keep a portfolio of your best work

**Transfer Student Advantages:**
✓ Life experience appeals to employers
✓ Strong work ethic and time management
✓ Clear career focus and motivation
✓ Diverse perspectives and backgrounds

**Building Your Brand:**
- Develop a 30-second elevator pitch
- Identify your unique value proposition
- Collect testimonials and references
- Create a professional online presence

**Common Mistakes to Avoid:**
❌ Waiting until senior year to start networking
❌ Only applying to "dream" internships
❌ Not following up after networking events
❌ Undervaluing your community college experience

What type of experience are you most interested in pursuing?"""
    
    def _handle_school_comparison(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**UC vs CSU: Career Impact Analysis**

**Academic Reputation & Career Outcomes:**

**UC System Advantages:**
🎓 **Research Focus:** Better for grad school preparation
🏢 **Industry Connections:** Strong ties to tech, finance, biotech
📊 **Alumni Networks:** Powerful networks in major industries
💰 **Starting Salaries:** 10-15% higher on average
🌟 **Brand Recognition:** National/international reputation

**CSU System Advantages:**
💼 **Practical Focus:** Hands-on, industry-ready curriculum  
🏭 **Local Industry Ties:** Strong regional employer relationships
💵 **Lower Debt:** Significantly lower tuition costs
👥 **Class Sizes:** Often smaller, more personalized attention
⚡ **Career Services:** Strong focus on job placement

**Field-Specific Recommendations:**

**Choose UC if you're interested in:**
- Graduate school/PhD programs
- Research careers
- Competitive industries (tech, finance, consulting)
- International opportunities
- Fields requiring prestige (medicine, law preparation)

**Choose CSU if you're interested in:**
- Direct entry to workforce
- Teaching (especially K-12)
- Regional employment
- Practical, applied programs
- Minimizing student debt

**Career Impact by Major:**

**Computer Science:**
- UC: Better for FAANG companies, startups, research
- CSU: Strong regional tech placement, practical skills

**Business:**
- UC: Better for consulting, investment banking
- CSU: Excellent for regional business, entrepreneurship

**Engineering:**
- UC: Research, grad school, cutting-edge companies
- CSU: Industry partnerships, practical application

**Education:**
- CSU: Superior teacher preparation programs
- UC: Better for educational research, administration

**Psychology:**
- UC: Better for research, grad school preparation
- CSU: Strong applied psychology, counseling focus

**Making Your Decision:**

**Consider Your Goals:**
- Career timeline (immediate work vs grad school)
- Geographic preferences
- Industry targets
- Financial considerations
- Learning style preferences

**Financial Analysis:**
- UC: Higher tuition but potentially higher earning
- CSU: Lower debt, faster ROI
- Consider 10-year financial impact, not just upfront costs

**Quality of Fit:**
- Visit campuses if possible
- Talk to current students and alumni
- Research specific program strengths
- Consider faculty expertise in your area

Both UC and CSU can lead to successful careers - the best choice depends on your specific goals, financial situation, and learning preferences.

What factors are most important to you in making this decision?"""
    
    def _handle_general_career_guidance(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Comprehensive Career Guidance for Transfer Students**

**Career Planning Framework:**

**1. Self-Discovery Phase**
🔍 **Assess Your Interests:** What subjects energize you?
💪 **Identify Your Strengths:** What comes naturally to you?
🎯 **Clarify Your Values:** What matters most in your work life?
🌟 **Define Success:** What does career fulfillment look like?

**2. Exploration Phase**
📚 Research industries and roles
🤝 Conduct informational interviews
💼 Attend career fairs and networking events
🎓 Talk to professors and career counselors

**3. Experience Phase**
🏢 Pursue internships and part-time work
🔬 Engage in research or projects
👥 Join professional organizations
📈 Build relevant skills and portfolio

**4. Decision Phase**
⚖️ Evaluate options against your criteria
📊 Consider market demand and growth
💰 Assess financial implications
🎯 Make informed choices about major/career path

**Transfer Student Success Strategies:**

**Leverage Your Unique Position:**
✓ Highlight your maturity and life experience
✓ Emphasize strong academic foundation from CC
✓ Showcase diverse perspectives and backgrounds
✓ Demonstrate financial responsibility and goal-setting

**Maximize Your Time at UC/CSU:**
- Connect with faculty in your field
- Utilize career services extensively
- Build meaningful relationships with classmates
- Seek leadership opportunities
- Maintain connections with CC mentors

**Long-term Career Planning:**
🚀 **Years 1-5:** Build foundational skills and experience
📈 **Years 6-15:** Develop expertise and leadership abilities
🎯 **Years 16+:** Pursue senior roles or entrepreneurial ventures

**Key Resources:**
- UC/CSU career centers (use them heavily!)
- Professional associations in your field
- LinkedIn Learning for skill development
- Industry publications and websites
- Alumni networks and mentorship programs

**Common Transfer Student Concerns:**

**"I'm behind my peers"**
→ You're not behind, you're on a different path with unique advantages

**"I don't have enough experience"**
→ Your CC experience, work history, and life skills count as experience

**"I'm older than other students"**
→ Employers value maturity, focus, and real-world perspective

**"I'm not sure what I want to do"**
→ This is normal! Use junior year to explore and clarify

Remember: Career success isn't just about the destination - it's about continuous learning, adaptation, and finding work that aligns with your values and strengths.

What specific aspect of career planning would you like to dive deeper into?"""