from typing import Dict, Any, List
from agents import Agent

class CourseDifficultyAgent:
    """Specialized agent for course planning and academic difficulty management for UC/CSU transfer students"""
    
    def __init__(self):
        self.agent = Agent(
            name="Academic Advisor",
            instructions="""You are a specialized Academic Advisor focused on course difficulty management for UC/CSU transfer students. Your expertise includes:

CORE RESPONSIBILITIES:
- Course sequencing and prerequisite planning
- Difficulty assessment and workload management
- Study strategies for challenging courses
- Time management and academic success skills
- Transfer requirement completion planning
- GPA management and academic recovery

KNOWLEDGE AREAS:
- UC/CSU transfer requirements (IGETC, CSU GE)
- Common prerequisite sequences by major
- Course difficulty patterns and student success rates
- Study techniques and learning strategies
- Academic support resources at UC/CSU
- Time management for working students

APPROACH:
- Assess student's academic background and goals
- Provide realistic course load recommendations
- Suggest specific study strategies for difficult subjects
- Connect students with appropriate support resources
- Help balance academic and life commitments

Focus exclusively on academic success for UC/CSU transfer students.""",
            model="4.1-nano",
            tools=[]
        )
        
        # Academic planning knowledge base
        self.academic_data = {
            'course_difficulty_levels': {
                'high_difficulty': {
                    'subjects': ['organic_chemistry', 'calculus_3', 'physics_with_calculus', 'accounting', 'statistics'],
                    'study_hours_per_week': 15,
                    'success_strategies': ['Form study groups', 'Use professor office hours', 'Start assignments early']
                },
                'moderate_difficulty': {
                    'subjects': ['college_algebra', 'general_chemistry', 'microeconomics', 'psychology', 'english_composition'],
                    'study_hours_per_week': 10,
                    'success_strategies': ['Regular review', 'Practice problems', 'Active reading']
                },
                'lower_difficulty': {
                    'subjects': ['art_history', 'intro_sociology', 'speech', 'pe_courses'],
                    'study_hours_per_week': 6,
                    'success_strategies': ['Consistent attendance', 'Basic note-taking', 'Participate in discussions']
                }
            },
            'transfer_requirements': {
                'igetc': {
                    'area_1': 'English Communication (3 courses)',
                    'area_2': 'Mathematical Concepts (1 course)',
                    'area_3': 'Arts and Humanities (3 courses)',
                    'area_4': 'Social Sciences (3 courses)', 
                    'area_5': 'Physical/Biological Sciences (2 courses + labs)',
                    'area_6': 'Languages Other Than English (proficiency)'
                },
                'major_prep': 'Varies by major - check assist.org for specific requirements'
            }
        }
    
    def handle_query(self, query: str, student_context: Dict[str, Any] = None) -> str:
        """Process course difficulty and academic planning queries"""
        query_lower = query.lower()
        
        if student_context is None:
            student_context = {}
        
        # Route to specific academic planning topic
        if any(word in query_lower for word in ['difficult', 'hard', 'struggling', 'failing']):
            return self._handle_difficulty_management(query, student_context)
        elif any(word in query_lower for word in ['study', 'how to', 'strategies', 'tips']):
            return self._handle_study_strategies(query, student_context)
        elif any(word in query_lower for word in ['course load', 'units', 'how many classes']):
            return self._handle_course_load_planning(query, student_context)
        elif any(word in query_lower for word in ['prerequisite', 'requirements', 'sequence']):
            return self._handle_prerequisite_planning(query, student_context)
        elif any(word in query_lower for word in ['time management', 'balance', 'schedule']):
            return self._handle_time_management(query, student_context)
        elif any(word in query_lower for word in ['gpa', 'grades', 'academic probation']):
            return self._handle_gpa_management(query, student_context)
        else:
            return self._handle_general_academic_guidance(query, student_context)
    
    def _handle_difficulty_management(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Managing Difficult Courses - Academic Success Strategies**

**Immediate Action Plan for Struggling Students:**

**Week 1-2: Assessment & Resources**
📊 Identify specific areas of difficulty
🏫 Meet with professor during office hours
📚 Connect with campus tutoring center
👥 Form or join study groups
📝 Review and adjust study methods

**High-Difficulty Course Strategies:**

**For STEM Courses (Math, Chemistry, Physics):**
✓ **Practice Daily:** 30-60 minutes of problem-solving
✓ **Conceptual Understanding:** Don't just memorize formulas
✓ **Sequential Learning:** Master each topic before moving on
✓ **Multiple Resources:** Textbook, online videos, study guides
✓ **Error Analysis:** Understand why you got problems wrong

**For Writing-Intensive Courses:**
✓ **Start Early:** Begin assignments immediately
✓ **Outline Everything:** Plan before writing
✓ **Multiple Drafts:** Never submit first draft
✓ **Writing Center:** Use campus writing support
✓ **Reading Strategies:** Active reading with notes

**For Memorization-Heavy Courses:**
✓ **Spaced Repetition:** Review material over time
✓ **Multiple Modalities:** Visual, auditory, kinesthetic
✓ **Association Techniques:** Connect new info to known concepts
✓ **Practice Testing:** Self-quiz regularly
✓ **Study Groups:** Teach others to reinforce learning

**Warning Signs You Need Help:**
🚨 Falling behind in multiple courses
🚨 Missing assignments or poor quiz scores
🚨 Feeling overwhelmed or anxious about academics
🚨 Considering dropping courses

**Campus Resources:**
- **Tutoring Centers:** Free peer and professional tutoring
- **Study Skills Workshops:** Learning strategy training
- **Academic Counseling:** Course planning and strategy
- **Supplemental Instruction:** Study sessions for difficult courses
- **Disability Services:** Accommodations if needed

**Damage Control Strategies:**
If you're already behind:
1. **Triage:** Focus on courses you can still pass
2. **Late Drop:** Consider strategic course withdrawal
3. **Incomplete Grades:** Negotiate extensions if appropriate
4. **Summer Recovery:** Plan to retake courses if needed

Remember: Struggling in difficult courses is normal! The key is getting help early and using effective strategies.

What specific course or subject are you finding most challenging?"""
    
    def _handle_study_strategies(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Proven Study Strategies for Transfer Students**

**Evidence-Based Learning Techniques:**

**1. Active Recall (Most Effective)**
📝 Test yourself without looking at notes
❓ Create questions and answer them
🔄 Explain concepts out loud to yourself
📋 Use flashcards for key terms and concepts

**2. Spaced Repetition**
📅 Review material at increasing intervals
⏰ Day 1 → Day 3 → Day 7 → Day 14 → Day 30
🧠 Strengthens long-term memory formation
📊 Use apps like Anki for spaced repetition

**3. Interleaving Practice**
🔀 Mix different types of problems/topics
📚 Don't study one subject for hours straight
🎯 Improves problem-solving flexibility
🧩 Practice identifying which method to use

**Subject-Specific Study Methods:**

**Mathematics & Sciences:**
- **Problem-solving practice:** Do problems without looking at solutions first
- **Concept mapping:** Connect ideas visually
- **Teaching method:** Explain processes step-by-step
- **Error analysis:** Understand mistakes deeply

**Social Sciences & Humanities:**
- **Cornell notes:** Organized note-taking system
- **Summarization:** Condense chapters into key points
- **Discussion groups:** Debate ideas with classmates
- **Essay outlining:** Plan before writing

**Languages:**
- **Immersion:** Surround yourself with the language
- **Daily practice:** 15-30 minutes consistently
- **Speaking practice:** Don't just read/write
- **Cultural context:** Learn beyond just vocabulary

**Time Management for Studying:**

**The 50/10 Rule:**
🕐 Study for 50 minutes
☕ Break for 10 minutes
🔄 Repeat for 3-4 cycles
🏃 Take longer break (30 minutes)

**Study Schedule Templates:**

**Heavy Course Load (15+ units):**
- 6-8 hours study time daily
- 2-3 study blocks per day
- 1 full day off per week

**Moderate Course Load (12-14 units):**
- 4-6 hours study time daily
- 2 study blocks per day
- Flexible weekend schedule

**Creating Your Study Environment:**
🏠 **Location:** Quiet, well-lit, organized
📱 **Distractions:** Phone in another room
🎵 **Background:** Silence or instrumental music
🪑 **Ergonomics:** Comfortable but alert position
📚 **Materials:** Everything within reach

**Study Group Best Practices:**
✓ **Size:** 3-5 people maximum
✓ **Preparation:** Everyone comes prepared
✓ **Structure:** Agenda and time limits
✓ **Teaching:** Take turns explaining concepts
✓ **Accountability:** Regular meeting schedule

**Exam Preparation Timeline:**

**2 Weeks Before:**
- Create comprehensive study guide
- Identify weak areas needing focus
- Form study group

**1 Week Before:**
- Practice tests under timed conditions
- Review and memorize key formulas/facts
- Get clarification on confusing topics

**Day Before:**
- Light review only (no cramming)
- Prepare materials for exam day
- Get good sleep (8+ hours)

**Day Of:**
- Eat protein-rich breakfast
- Arrive early to reduce anxiety
- Quick warm-up review

What specific study challenges are you facing?"""
    
    def _handle_course_load_planning(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Course Load Planning for Transfer Students**

**Recommended Unit Loads:**

**Full-Time Student Guidelines:**
- **First Semester at CC:** 12-15 units (get acclimated)
- **Experienced CC Student:** 15-18 units
- **Pre-Transfer (Final Year):** 12-15 units (focus on grades)
- **At UC/CSU:** 13-16 units (adjust to new environment)

**Part-Time Student Guidelines:**
- **Working 20+ hours/week:** 6-9 units
- **Working 30+ hours/week:** 3-6 units
- **Family obligations:** Adjust based on responsibilities

**Course Difficulty Balancing:**

**High Difficulty Courses (limit 1-2 per semester):**
- Organic Chemistry, Calculus III, Physics with Calculus
- Upper-division major courses
- Research methods, statistics
- Foreign language intensive courses

**Moderate Difficulty Courses (2-3 per semester):**
- General Chemistry, College Algebra
- Psychology, Sociology, Economics
- English Composition, Speech
- Introduction to major courses

**Lower Difficulty Courses (use as GE fillers):**
- Art History, Music Appreciation
- Physical Education courses  
- Some ethnic studies courses
- Basic computer applications

**Strategic Course Planning:**

**Semester Balancing Examples:**

**Balanced Load (15 units):**
- High difficulty: Calculus II (5 units)
- Moderate: Psychology (3 units)
- Moderate: English Composition (3 units)
- Lower: Art History (3 units)
- Easy: PE Course (1 unit)

**STEM-Heavy Load (16 units):**
- High: Organic Chemistry + Lab (5 units)
- Moderate: Statistics (4 units)
- Moderate: Physics (4 units)
- Lower: General Education course (3 units)

**Prerequisites and Sequencing:**

**Math Sequence Planning:**
Basic Math → Algebra → Trigonometry → Calculus I → Calculus II → Calculus III
*Plan 1-2 semesters per level depending on preparation*

**Science Sequence:**
General Chemistry I & II → Organic Chemistry I & II → Biochemistry
*Take physics alongside, not after*

**Transfer Timeline Optimization:**

**Two-Year Plan:**
- **Year 1:** Complete basic requirements, explore majors
- **Year 2:** Focus on major prerequisites, maintain high GPA

**Three-Year Plan (recommended for working students):**
- **Year 1:** Adjust to college, build study skills
- **Year 2:** Core requirements and prerequisites  
- **Year 3:** Complete transfer requirements, applications

**Warning Signs of Overload:**
🚨 Consistently behind in multiple courses
🚨 Sleep deprivation (less than 6 hours regularly)
🚨 Declining grades across all courses
🚨 Missing assignments or skipping classes
🚨 High stress levels affecting health

**Course Load Adjustment Strategies:**
✓ **Late Add/Drop:** Use first 2 weeks to assess difficulty
✓ **Strategic Withdrawal:** Better to withdraw than fail
✓ **Summer Courses:** Catch up or get ahead
✓ **Winter Intersession:** Knock out difficult courses solo
✓ **Online Options:** May offer more flexibility

**Special Considerations:**

**Working Students:**
- Schedule courses on consecutive days
- Choose morning or evening blocks consistently
- Consider online hybrid courses
- Plan for reduced social/extracurricular time

**Parents/Caregivers:**
- Arrange childcare backup plans
- Choose courses with flexible attendance policies
- Build support network with other student parents
- Utilize campus family resources

**First-Generation Students:**
- Start conservatively with course load
- Use campus support services extensively
- Connect with mentors and advisors
- Don't hesitate to ask for help

How many units are you currently taking, and what's your work/life situation?"""
    
    def _handle_prerequisite_planning(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Prerequisites and Transfer Requirement Planning**

**Essential Planning Resources:**
🌐 **ASSIST.org:** Official transfer articulation system
📋 **IGETC:** Intersegmental General Education Transfer Curriculum
🎓 **CSU GE:** California State University General Education
📊 **Major preparation:** Specific courses required for your major

**Transfer Requirement Categories:**

**1. General Education Requirements:**

**IGETC (for UC transfers):**
- **Area 1:** English Communication (2 courses)
- **Area 2:** Mathematical Concepts (1 course)  
- **Area 3:** Arts & Humanities (3 courses from 2 areas)
- **Area 4:** Social Sciences (3 courses from 2 areas)
- **Area 5:** Physical/Biological Sciences (2 courses + labs)
- **Area 6:** Language Other Than English (proficiency level)

**CSU GE (for CSU transfers):**
- **Area A:** English Language & Critical Thinking (3 courses)
- **Area B:** Scientific Inquiry & Quantitative Reasoning (3 courses)
- **Area C:** Arts & Humanities (3 courses)
- **Area D:** Social Sciences (3 courses)
- **Area E:** Lifelong Learning (3 courses)

**2. Major Preparation Requirements:**
✓ Prerequisite courses specific to your major
✓ Recommended courses for competitive applicants
✓ Sequence requirements (take courses in order)

**Common Prerequisite Sequences:**

**Business Majors:**
1. College Algebra → Statistics
2. Financial Accounting → Managerial Accounting  
3. Microeconomics → Macroeconomics
4. Business Law, Business Communications

**STEM Majors:**
1. Algebra → Trigonometry → Calculus I → II → III
2. General Chemistry I → II → Organic Chemistry
3. General Physics I → II (algebra or calculus-based)
4. Programming languages specific to major

**Psychology Majors:**
1. Introduction to Psychology
2. Statistics → Research Methods
3. Abnormal Psychology, Developmental Psychology
4. Biological Psychology

**Engineering Majors:**
1. Math sequence through Differential Equations
2. Chemistry + Physics sequences
3. Introduction to Engineering
4. Programming/Computer Science

**Strategic Planning Timeline:**

**Freshman Year (CC):**
- Complete English and Math requirements early
- Explore different majors through introductory courses
- Focus on building strong GPA foundation
- Meet with counselors to understand transfer paths

**Sophomore Year (CC):**
- Complete major prerequisites
- Finish general education requirements
- Take challenging courses (maintain manageable load)
- Prepare for transfer applications

**Course Sequencing Strategy:**

**Priority 1 (Take First):**
- English Composition (prerequisite for many courses)
- College-level Math (often prerequisite for sciences)
- Introduction to Major courses

**Priority 2 (Middle):**
- Major prerequisites with sequences
- Laboratory sciences
- Foreign language (if required)

**Priority 3 (Final Year):**
- Upper-division GE courses
- Additional major preparation
- Electives and interest courses

**Common Planning Mistakes:**

❌ **Waiting too long for math sequence**
→ Start math early, even if placement is low

❌ **Not checking articulation agreements**
→ Use ASSIST.org for every course decision

❌ **Taking courses at wrong campus**
→ Verify transferability before enrolling

❌ **Ignoring prerequisite chains**
→ Map out 2-3 semester sequences in advance

❌ **Overloading difficult prerequisites**
→ Balance challenging courses across semesters

**Planning Tools and Resources:**

**Academic Planning:**
- Meet with counselors each semester
- Use degree planning software (MyPlan, DegreeWorks)
- Create backup plans for different majors
- Track progress with checklists

**Course Selection:**
- Read course descriptions carefully
- Check professor ratings and reviews
- Consider course scheduling (time conflicts)
- Have backup course options

**Transfer Application Timing:**
- **UC Application:** Opens August 1, due November 30
- **CSU Application:** Opens October 1, due November 30
- Complete major prep by fall before transfer
- Spring admission available at some campuses

What major are you planning to transfer into? I can help you map out the specific prerequisite sequence."""
    
    def _handle_time_management(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Time Management for Transfer Students**

**Time Management Framework:**

**The Transfer Student Challenge:**
- Juggling work, family, and school responsibilities
- Limited time compared to traditional students  
- Need for maximum efficiency in studying
- Balancing current courses with transfer planning

**Priority Management System:**

**Level 1 - Critical (Do First):**
🎯 Assignment deadlines and exam dates
🎯 Transfer application deadlines
🎯 Work schedule commitments
🎯 Family obligations and emergencies

**Level 2 - Important (Schedule Regularly):**
📚 Daily study time for each course
📝 Transfer requirement planning
💼 Career development activities
🏥 Personal health and self-care

**Level 3 - Beneficial (When Time Allows):**
👥 Social activities and networking
🎨 Hobbies and personal interests
📺 Entertainment and relaxation
🏃 Additional fitness activities

**Weekly Schedule Templates:**

**Full-Time Student + Part-Time Work:**
- **Monday-Friday:** Classes + 3-4 hours study
- **Weekend:** Work shifts + catch-up study
- **Total study time:** 25-30 hours/week

**Part-Time Student + Full-Time Work:**
- **Evening classes:** 2-3 courses maximum
- **Weekend intensive study:** 8-10 hours
- **Daily review:** 30-60 minutes
- **Total study time:** 15-20 hours/week

**Student Parent:**
- **Early morning study:** 5-7 AM (quiet time)
- **Study during childcare:** Maximize efficiency
- **Evening review:** After kids' bedtime
- **Weekend family integration:** Educational activities

**Daily Time Management:**

**Time Blocking Technique:**
🕐 **Morning Block (2-3 hours):** Hardest subjects
🕐 **Afternoon Block (1-2 hours):** Review and homework
🕐 **Evening Block (1 hour):** Light reading, planning

**Micro-Learning Sessions:**
- **15-minute breaks:** Review flashcards
- **Commute time:** Listen to recorded lectures
- **Waiting periods:** Read course materials
- **Before bed:** Quick review of day's learning

**Productivity Strategies:**

**The Pomodoro Technique:**
⏱️ 25 minutes focused study
☕ 5-minute break
🔄 Repeat 4 cycles
🏃 30-minute long break

**Time Audit Exercise:**
📊 Track actual time use for 1 week
🎯 Identify time wasters and inefficiencies
📈 Optimize based on findings
🔄 Adjust schedule accordingly

**Technology Tools:**

**Planning Apps:**
- **Google Calendar:** Class and work schedules
- **Todoist/Any.do:** Task management
- **Forest:** Focus timer with gamification
- **RescueTime:** Automatic time tracking

**Study Apps:**
- **Notion:** All-in-one workspace
- **Anki:** Spaced repetition flashcards
- **Khan Academy:** Supplemental learning
- **Grammarly:** Writing assistance

**Overcoming Common Time Challenges:**

**Problem: "I don't have enough time to study"**
✅ **Solution:** Time audit + micro-learning + efficiency improvements

**Problem: "I'm always behind on assignments"**
✅ **Solution:** Use assignment calendar + start immediately + break large tasks down

**Problem: "I can't balance work and school"**
✅ **Solution:** Communicate with employers + strategic course selection + support systems

**Problem: "Family responsibilities interfere"**
✅ **Solution:** Family schedule coordination + childcare arrangements + communicate boundaries

**Energy Management:**

**Peak Performance Hours:**
🌅 **Morning people:** Schedule hardest subjects early
🌙 **Night owls:** Use evening hours for intensive study
⚡ **Consistent schedule:** Train your brain for optimal times

**Avoiding Burnout:**
- Schedule regular breaks and rest days
- Maintain physical exercise routine
- Preserve time for relationships
- Practice stress management techniques

**Academic Calendar Planning:**

**Semester Preparation:**
- Map out all major deadlines first week
- Identify busy periods and plan accordingly
- Schedule study intensives before exams
- Build in buffer time for unexpected challenges

**Transfer Timeline Integration:**
- **Fall semester:** Focus on grades + applications
- **Spring semester:** Maintain GPA + plan transition
- **Summer:** Prepare for transfer school

What specific time management challenges are you facing?"""
    
    def _handle_gpa_management(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**GPA Management and Academic Recovery**

**GPA Requirements for Transfer:**

**UC System:**
- **Minimum:** 2.4 GPA for California residents
- **Competitive:** 3.0-3.5+ for most majors
- **Highly Competitive:** 3.7+ for impacted majors (Business, Engineering, etc.)
- **TAG Programs:** 3.2-3.5 GPA guarantees admission to most UCs

**CSU System:**
- **Minimum:** 2.0 GPA for California residents
- **Competitive:** 2.5-3.0+ for impacted majors
- **Local Area:** Priority admission with 2.5+ GPA
- **Merit Scholarships:** 3.5+ GPA typically required

**GPA Calculation Strategies:**

**Understanding Your GPA:**
- **Overall GPA:** All college coursework
- **Major GPA:** Courses specific to your major
- **Transferable GPA:** Only UC/CSU transferable courses
- **Last 60 Units:** Some schools focus on recent performance

**Grade Point Values:**
- A = 4.0, B = 3.0, C = 2.0, D = 1.0, F = 0.0
- Plus/minus grades: A- = 3.7, B+ = 3.3, etc.
- **Pass/No Pass:** P doesn't affect GPA, NP counts as F

**GPA Recovery Strategies:**

**If Your GPA is Below 2.5:**
🚨 **Immediate Actions:**
- Meet with academic counselor immediately
- Consider reducing course load
- Focus on passing all current courses
- Seek tutoring for struggling subjects

📈 **Recovery Plan:**
- Retake failed courses (grade replacement)
- Take easier GE courses to boost GPA
- Consider Pass/No Pass for risky courses
- Plan 2-3 additional semesters for recovery

**If Your GPA is 2.5-3.0:**
✅ **Maintenance Strategy:**
- Avoid high-risk courses this semester
- Focus on B+ or better in all courses
- Complete prerequisites with strong grades
- Consider summer courses for GPA boost

**If Your GPA is 3.0+:**
🎯 **Optimization Strategy:**
- Aim for A's in major prerequisite courses
- Take challenging courses strategically
- Consider Honors program participation
- Maintain consistency across all courses

**Course Selection for GPA Management:**

**GPA Boosting Courses:**
- Art History, Music Appreciation
- Physical Education courses
- Some Ethnic Studies courses
- Introduction to Human Development
- Creative Writing, Film Studies

**GPA Risk Courses (approach carefully):**
- Organic Chemistry, Physics with Calculus
- Accounting, Statistics
- Foreign Language intensives
- Upper-division Mathematics
- Laboratory-heavy sciences

**Strategic Grade Management:**

**Grade Recovery Options:**
- **Course Repetition:** Retake for grade replacement
- **Academic Renewal:** Petition to exclude old poor grades
- **Pass/No Pass:** Protect GPA for difficult but required courses
- **Course Withdrawal:** Strategic W's better than F's

**Timing Considerations:**
- **Fall Grades:** Most important for transfer applications
- **Spring Grades:** Final chance to boost GPA
- **Summer Courses:** Opportunity for focused improvement
- **Winter Intersession:** Intensive courses with full attention

**Academic Probation Recovery:**

**If on Academic Probation (GPA below 2.0):**
⚠️ **Immediate Requirements:**
- Meet with counselor within first week
- Develop academic success plan
- Utilize all campus support services
- Consider reducing to minimum course load

📋 **Recovery Timeline:**
- **Semester 1:** Focus solely on passing courses
- **Semester 2:** Aim for 2.5+ GPA this term
- **Semester 3:** Achieve overall 2.0+ GPA to clear probation

**Study Strategy for GPA Improvement:**

**High-Impact Activities:**
- Attend every class session
- Complete all assignments on time
- Use professor office hours regularly
- Form study groups for difficult courses
- Start assignments immediately when assigned

**Grade Tracking:**
📊 Calculate GPA after each assignment/exam
📈 Project final course grades mid-semester
🎯 Identify courses needing extra attention
📋 Plan grade improvement strategies

**Communication with Instructors:**
- Introduce yourself early in semester
- Ask about extra credit opportunities
- Request clarification on expectations
- Communicate challenges before they become critical

**Long-term GPA Planning:**

**Transfer Application Strategy:**
- Apply to range of schools matching your GPA
- Emphasize upward grade trend in personal statement
- Consider alternative admission programs
- Have backup plans for different GPA scenarios

**Post-Transfer Considerations:**
- UC/CSU admission GPA ≠ graduation GPA (fresh start)
- Focus on learning, not just grades
- Build relationships with professors
- Maintain habits that led to improvement

What's your current GPA situation, and what specific grade challenges are you facing?"""
    
    def _handle_general_academic_guidance(self, query: str, context: Dict[str, Any]) -> str:
        return f"""**Comprehensive Academic Success Guide for Transfer Students**

**Academic Success Framework:**

**Foundation Elements:**
🎯 **Clear Goals:** Know why you're pursuing transfer
📚 **Study Systems:** Consistent, effective methods
⏰ **Time Management:** Balance competing priorities
🤝 **Support Networks:** Utilize available resources
📈 **Progress Tracking:** Monitor and adjust strategies

**Transfer Student Advantages:**
✅ **Maturity:** Life experience brings focus and perspective
✅ **Motivation:** Clear goals and investment in success
✅ **Efficiency:** Limited time creates urgency and purpose
✅ **Resilience:** Overcoming obstacles builds mental toughness
✅ **Diversity:** Varied backgrounds enrich learning experience

**Academic Planning Essentials:**

**Semester Planning Process:**
1. **Course Selection:** Balance difficulty, requirements, interests
2. **Schedule Optimization:** Consider work, family, commute
3. **Resource Identification:** Tutoring, study groups, office hours
4. **Goal Setting:** Specific, measurable academic targets
5. **Contingency Planning:** Backup options for challenges

**Academic Success Habits:**

**Daily Practices:**
📖 **Active Reading:** Engage with texts, take notes
✍️ **Daily Review:** 15-30 minutes per course
❓ **Question Generation:** Create your own practice problems
🗣️ **Concept Explanation:** Teach ideas to others
📝 **Planning Updates:** Adjust schedule based on progress

**Weekly Practices:**
📊 **Progress Assessment:** Review grades, understanding
🎯 **Goal Adjustment:** Modify strategies based on results
🤝 **Collaboration:** Study groups, peer discussions
💪 **Self-Care:** Rest, exercise, stress management
📅 **Upcoming Preparation:** Plan for next week's challenges

**Support System Development:**

**Academic Support:**
- **Professors:** Office hours, clarification, guidance
- **Teaching Assistants:** Additional help, practice sessions
- **Tutoring Centers:** Subject-specific assistance
- **Study Groups:** Peer learning and motivation
- **Academic Counselors:** Planning and problem-solving

**Personal Support:**
- **Family/Friends:** Understanding and encouragement
- **Mental Health Services:** Stress and anxiety management
- **Financial Aid:** Reducing financial stress
- **Childcare:** For student parents
- **Healthcare:** Maintaining physical wellness

**Common Academic Challenges:**

**Challenge: Imposter Syndrome**
💭 *"I don't belong here"*
✅ **Response:** Focus on your achievements, seek mentorship, remember you earned your place

**Challenge: Time Constraints**  
⏰ *"I don't have enough time"*
✅ **Response:** Time audit, efficiency improvements, micro-learning, prioritization

**Challenge: Academic Preparation Gaps**
📚 *"I'm behind other students"*
✅ **Response:** Supplemental resources, tutoring, summer preparation, foundation building

**Challenge: Multiple Responsibilities**
🔄 *"Too many competing priorities"*
✅ **Response:** Communication, boundary setting, support systems, strategic planning

**Technology and Learning:**

**Essential Tools:**
- **Learning Management Systems:** Canvas, Blackboard navigation
- **Note-Taking Apps:** OneNote, Notion, traditional methods
- **Time Management:** Calendar apps, task managers
- **Study Apps:** Flashcards, practice quizzes, video resources
- **Communication:** Email etiquette, video conferencing

**Academic Integrity:**

**Understanding Expectations:**
- Proper citation and source attribution
- Collaboration vs. individual work boundaries
- Academic honesty in all assignments
- Time management to avoid desperation cheating
- Seeking help appropriately

**Transfer Preparation Integration:**

**Academic Performance:**
- Maintain competitive GPA for target schools
- Excel in major prerequisite courses
- Demonstrate upward grade trends
- Build relationships with professors for recommendations

**Holistic Development:**
- Leadership roles in clubs/organizations
- Community service and volunteer work
- Research or internship experiences
- Personal growth and self-awareness

**Long-term Academic Vision:**

**Beyond Transfer:**
- Preparation for upper-division coursework
- Research and graduate school readiness
- Professional development planning
- Lifelong learning mindset
- Alumni network building

Remember: Academic success isn't just about grades—it's about developing the skills, knowledge, and relationships that will serve you throughout your educational journey and career.

What specific aspect of academic success would you like to focus on developing?"""