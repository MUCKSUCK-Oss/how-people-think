# How universities and education sellers trick students: research (night of 11 Nov 2026)
*Collected BEFORE designing the new simulation. Sources are news, regulators, video investigations and research papers. Numbers come from summaries and reports, **[CHECK]** the originals before quoting them in the paper.*

---
## A. India

### 1. Placement and salary hype (the biggest pattern)
- **Coaching ad rules, 13 Nov 2024:** the Central Consumer Protection Authority (CCPA) banned coaching institutes from claiming "100% selection" or "100% job guarantee". It also required disclaimers in the **same font size** as the claim, in a visible place. The CCPA fined 19 institutes about ₹61.6 lakh (Lok Sabha answer, Dec 2024). These rules cover coaching only, **not colleges**.
- **Coaching institutes "buy" toppers:** surveys and reports say institutes pay top-rank students to appear in their ads, and add students to their "results" without consent (The Wire; The Quint). Ads show ranks but never the share of all enrolled students who got selected.
- **"Highest package" vs median:** colleges advertise the single highest salary. One star student can produce it, while the typical graduate earns far less. Careers360 and others warn that the highest package "is not an accurate measure". India's NIRF data includes medians, but families rarely see them in ads.
- **Hidden outcomes:** ThePrint reports that **almost half of engineering graduates** struggled to get campus placements (2019–23). The often-quoted "80% of engineers unemployable" comes from Aspiring Minds, a company that sells job tests, so treat it as a vendor estimate.
- **Skills:** Loyalka et al. 2021 (*Nature Human Behaviour*) followed CS/EE students in China, India, Russia and the USA. Indian students started behind in critical thinking and **did not gain** critical-thinking skills over 4 years. That suggests many degrees deliver less than they promise.

### 2. Too many seats, weak colleges, and the push to fill them
- 2019–24: **6.49 million** engineering seats sanctioned, **1.94 million left empty** (ThePrint). Empty seats are most common in rural private colleges. **An empty seat = lost fees, so these colleges have a strong reason to market hard.**
- AICTE closed 58 engineering colleges in 2025–26, and at least 50 a year have shut since 2015–16.

### 3. Fake universities and fraud
- **UGC list (Oct 2025): 22 fake universities.** 10 are in Delhi; their degrees aren't valid.
- **NRI-quota fraud:** the Enforcement Directorate found private medical colleges in West Bengal and Odisha admitted ineligible students on **fake NRI documents** made with agents. It froze ₹6.42 crore. One report says about **18,000** such MBBS admissions nationally **[CHECK]**. "Capitation fees" of ₹50 lakh–₹1 crore are mentioned in an opinion piece **[CHECK]**.

### 4. Loans
- RBI Financial Stability Report (June 2024): **education loans had the highest default rate of all personal loans** (3.6% NPA, against 1.1% for housing). Public-sector bank education-loan NPAs fell from 7% (FY21) to 2% (FY25).
- An RBI working paper: loans with **higher interest and no collateral** default more, which fits poorer families borrowing for weaker colleges.

### 5. Who decides: the student or the parents?
- **The evidence is mixed and weak.** A Shiksha survey found 70% of students said engineering was "their choice", and only 10% said parents forced it (a self-selected website sample). Interviews at BITS Pilani (2013) found parents, especially fathers, "played a big role". A small 2024 student study found girls' choices closely match parents' wishes.
- **Design decision:** simulate **both students and parents** as separate AI people. Where money is involved (loans, selling land), parents usually have the final say, as in every case in the CBC and DW videos.

---
## B. Abroad

### 6. Study-abroad agents (Canada, UK, Germany): the strongest real "trap" for Indian families
- **CBC *The Fifth Estate*, "How recruiters in India use false promises to lure students to Canada"** (3M views; transcript read in full):
  - A Punjabi farmer **sold two trucks** to raise about CA$28,000 for his daughter. "The average Punjabi family would have to work **74 years** to pay one year's tuition."
  - Colleges charge international students about **5× domestic tuition**. International students put more money into Ontario public colleges' budgets than the Ontario government does.
  - **Agents are paid by colleges (up to $2,000 per student) AND by families.** A hidden camera recorded agents steering a family away from a known college toward a small career college that likely pays a higher commission.
  - **Agent promises:** "No English, no problem"; "guaranteed visa"; "you can get an office job anywhere in Toronto"; "no problem getting permanent residency". The platform's co-founder agreed on camera that the PR promise is "absolutely wrong".
  - **Alpha College:** 100% international, 99% from India. It had space for about 400 students but enrolled 2,500, then 5,000, and deferred students mid-course. One student hadn't seen her college for 9 months.
  - **Reality:** working 50+ hours a week at minimum wage, 15 people in one house, mental-health crises; a Brampton funeral home sends back **4–5 bodies of international students a month**.
  - Australia, New Zealand, the UK and Ireland signed an agent code of conduct. **Canada didn't.**
- **Fake admission letters (2023):** a Jalandhar agent (Brijesh Mishra) allegedly sold fake Canadian college offer letters for up to ₹20 lakh each. Students found out years later at the PR stage. About 70–80 got deportation notices (early "700" reports were too high); Mishra was arrested in June 2023.
- **UK:** universities pay agents **10–30% of first-year fees**. *The Times* undercover recorded agents saying weak students could get in via foundation courses; Universities UK announced a review.
- **Germany (DW, "Debt, exploitation, burnout", 2M views; transcript read):** Indian students in Germany number nearly 60,000 (2025). Many are sold expensive **private** universities (€18,000–25,000) via platforms like upGrad, while public universities charge almost nothing. One student found the "university" was a rented office building; he then delivered Amazon parcels below minimum wage and paid inflated rent to brokers.

### 7. USA: when job-placement claims were proven false
- **DeVry (2016):** paid **$100 million** (FTC) over "90% of graduates got jobs in their field within 6 months". The count included people who kept their old jobs or got jobs outside their field. DeVry denied wrongdoing.
- **Corinthian Colleges:** the Education Department found it **falsified job-placement rates**. It allegedly counted a "placement" as any job lasting one day, with 947 documented misrepresentations at one campus. A California judgment of $1.1 billion; the US forgave **$5.8 billion** of students' loans (2022).
- **US student debt:** about $1.8–1.9 trillion; around 9.5 million federal borrowers in default (2026). **For-profit colleges** have far more defaults than their share of students: 19% of repayment loans but 29% of defaults (pre-pandemic).

---
## C. Research on why the tricks work

| Finding | Study | What it means for the simulation |
|---|---|---|
| **People act on wrong beliefs about salaries**; giving true earnings information changed schooling decisions | Jensen 2010, *QJE* (Dominican Republic RCT): +0.20–0.35 years of school. But **no effect for the poorest**, because they couldn't afford it anyway | **Information can protect**, but money limits matter. Test a "true information shown" version |
| **Rankings move applications** because they're easy to see (salience) | Luca & Smith 2013: one rank up = about 1% more applications | Rank and award badges are a real lever |
| **Gatekeepers with hidden incentives** | CBC; UK agent commissions of 10–30% | A **"counsellor/agent paid per admission"** version, with and without disclosure |
| **Parents' wishes shape choices** | Shiksha (mixed); NHSJS 2024 (girls) | Include parents as decision-makers |
| **The quiet trick beats the loud one** | Our earbuds pilot; university run 1 (social proof worked, hype was called out); SusBench 2025 | Expect agents and relatives (people) to work better than ad banners |
| **Disclosure laws** | CCPA 2024: same font size for disclaimers | A **"disclosure"** version to test whether the law's fix works |

## D. Lessons for the new scenario (from run 1's mistake)
1. **Show what families really see.** Real ads don't show the median salary or agent commissions. The control should be "the brochure as families see it", and a separate version should add the **honest numbers**.
2. **Use realistic, closer options.** Not ₹18L vs ₹4L with almost equal outcomes. Real choices are ₹4–5L vs ₹10–12L, where the private college looks shinier and the outcome difference is unclear.
3. **Include abroad.** The **study-abroad agent** is the strongest documented trap (CBC, DW, the fake-letter case).
4. **The people:** students AND parents.
5. **The real tricks to test:**
   - highest-package/"100% placement assistance" hype
   - an agent or counsellor paid per admission
   - "PR easy / office job guaranteed"
   - relatives and village social proof ("300 youth from your village went")
   - booking-fee deadlines
   - **plus the fix:** honest disclosure
