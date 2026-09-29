"""One-screen navigation to the nutrition curriculum and primary references."""
import streamlit as st
from content import LESSONS, SOURCES

# Rows align with LESSONS in content.py. The key metric column is deliberately
# specific only where a general-purpose quantitative reference is justified.
BRIEFS = [
("Eat varied foods across days", "Don't chase one superfood", "Myth: one food fixes health. Fact: repeated patterns matter.", "Food groups across the week", "Record three typical days"),
("Add produce and protein to a familiar meal", "Don't force a fixed plate ratio", "Myth: every plate must be identical. Fact: context changes portions.", "Vegetables/fruit, protein, starch on plate", "Build one rice/dal/vegetable meal"),
("Choose the quality and amount of carbs and fats", "Don't cut an entire macro by default", "Myth: carbs are always bad. Fact: source and portions matter.", "Energy estimate: carb/protein 4, fat 9 kcal/g", "Inspect one meal's macro sources"),
("Include a useful protein source", "Don't assume everyone needs powder", "Myth: powder is essential. Fact: foods often suffice.", "Protein-containing foods in regular meals; personal target varies", "List protein foods in two meals"),
("Pair starch with legumes and vegetables", "Don't assume whole grain makes portion irrelevant", "Myth: brown rice has no glucose impact. Fact: quantity matters.", "Starch portion and fibre-rich foods", "Compare two familiar breakfasts"),
("Prefer unsaturated sources often", "Don't judge heart health by one food", "Myth: one spoon of ghee decides risk. Fact: pattern matters.", "Saturated fat and sodium on labels", "Compare repeated oil and snack choices"),
("Plan iron, B12, calcium and vitamin D sources", "Don't treat a lab result with a generic multivitamin", "Myth: all deficiencies need the same pill. Fact: cause and dose differ.", "Specific nutrient intake, tests when indicated", "Bring food history and results to care visit"),
("Use water as a default drink", "Don't impose one fluid target on everyone", "Myth: everyone needs eight glasses. Fact: needs vary.", "Drink pattern and added-sugar grams", "Review one day's drinks"),
("Multiply label values by servings eaten", "Don't infer healthfulness from 'natural'", "Myth: package claim is enough. Fact: label details matter.", "≤5% DV low; ≥20% DV high per serving", "Compare two labels at equal servings"),
("Clean, separate, cook, chill", "Don't rely on smell or reheating to fix unsafe storage", "Myth: color proves meat is safe. Fact: use a thermometer.", "Temperature and refrigeration time", "Check kitchen separation and thermometer"),
("Read allergen labels each time", "Don't assume tiny exposure is safe", "Myth: a small amount is always harmless. Fact: severe allergy can be dangerous.", "Ingredients, cross-contact and emergency plan", "Review household allergy plan"),
("Use familiar cooking methods and spices", "Don't present a spice as disease treatment", "Myth: traditional spice cures disease. Fact: culinary use is different.", "Added oil/salt and food safety", "Adapt one repeatable family recipe"),
("Plan, shop and prep repeatable meals", "Don't leave cooked perishables out too long", "Myth: every day must be perfect. Fact: review the pattern.", "Food-group variety and safe storage", "Plan two lunches from shared staples"),
("Fit meals to conditions and treatment", "Don't use one online diet for all diagnoses", "Myth: one diet treats every condition. Fact: plans differ.", "Relevant clinical measures and prescribed plan", "Prepare three dietitian/clinician questions"),
("Check a supplement's exact claim, dose and risk", "Don't replace needed treatment", "Myth: natural means safe. Fact: products can interact or harm.", "Dose, upper limit and medication interactions", "Look up product in NIH fact sheets"),
]
EXTRA = [
("🧮 Kitchen tools", "Estimate plate shares and label totals", "Don't treat estimates as a prescription", "Myth: calculator output is a diagnosis. Fact: it is arithmetic.", "Servings × per-serving grams or mg", "Try a package label", "FDA added-sugar label"),
("📚 Sources", "Trace a claim to its original authority", "Don't rely on testimonials alone", "Myth: popularity proves benefit. Fact: evidence quality matters.", "Source date, population and outcome", "Open one primary source", "WHO healthy diet"),
("⚖️ Compare approaches", "Use evidence-based nutrition for health decisions", "Don't substitute a remedy for care", "Myth: allopathy/homeopathy are cooking styles. Fact: neither is.", "Evidence and safety for the exact claim", "Compare a specific claim", "NCCIH homeopathy"),
("🌿 Ayurveda in the kitchen", "Enjoy suitable traditional meals", "Don't assume herbs/minerals are harmless", "Myth: tradition proves a cure. Fact: outcomes need testing.", "Ingredients, adequacy, interactions", "Review one traditional recipe", "NCCIH Ayurveda"),
("🧪 Homeopathy & decisions", "Seek proven care for illness", "Don't delay diagnosis or treatment", "Myth: homeopathy treats disease reliably. Fact: evidence does not support that.", "Clinical outcome, delay and interaction risks", "Check the claimed indication", "NCCIH homeopathy"),
    ("🧭 Health approaches", "Match the intervention to the condition", "Don't assume a broad label proves effectiveness", "Myth: all approaches work equally. Fact: evidence is practice-specific.", "Benefit, harm and treatment delay", "Compare the exact proposal with a primary source", "NCCIH integrative health"),
]
REFERENCES = [
("WHO healthy diet", "Fruit and vegetables", "≥400 g/day for people older than 10", "General population goal; younger children have different amounts", SOURCES["WHO healthy diet"]),
("WHO healthy diet", "Naturally occurring dietary fibre", "≥25 g/day for people older than 10", "Food sources; younger children have different amounts", SOURCES["WHO healthy diet"]),
("WHO healthy diet", "Free sugars", "<10% of energy; 50 g at 2,000 kcal", "Free sugars include honey, syrups and juice; not a universal gram target", SOURCES["WHO healthy diet"]),
("WHO sodium reduction", "Salt", "<5 g/day for adults (≈2,000 mg sodium)", "Total from cooking, packaged and restaurant foods", "https://www.who.int/news-room/fact-sheets/detail/sodium-reduction"),
("FDA % Daily Value guide", "Nutrient per labeled serving", "≤5% DV low; ≥20% DV high", "Check serving size; higher is desirable for some nutrients, lower for others", "https://www.fda.gov/food/nutrition-facts-label/lows-and-highs-percent-daily-value-nutrition-facts-label"),
]
SAFETY = [
("Poultry", "165°F / 74°C"),
("Ground meat", "160°F / 71°C"),
("Whole cuts of beef, pork, lamb", "145°F / 63°C + 3-minute rest"),
("Leftovers", "165°F / 74°C"),
]
SAFETY_URL = "https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures"

def render():
    st.header("📌 Master nutrition cheatsheet")
    st.caption("Quick reference across all lessons and tools · General education, not a personalized target or treatment plan")
    a,b,c=st.columns(3)
    a.metric("Lessons summarized", len(LESSONS))
    b.metric("Practical reference rows", len(REFERENCES))
    c.metric("Other tabs summarized", len(EXTRA)+1)
    st.info("Start with one change you can repeat: add a useful food group, check a label or handle food more safely. Open the detailed tab and original source for context.")
    rows=[]
    for lesson,brief in zip(LESSONS,BRIEFS):
        do,dont,myth,metric,next_step=brief
        rows.append({"Topic":lesson["title"],"Level":lesson["level"],"Core takeaway":lesson["takeaway"],"Do ✅":do,"Don't ⛔":dont,"Myth versus fact 💡":myth,"Key metric to follow 📏":metric,"Suggested next step ➡️":next_step,"Important context": "Individualize for diagnoses, medicines and age." if lesson["level"]=="Advanced" else "Review pattern and personal needs.","Primary source":SOURCES[lesson["sources"][0]]})
    rows.append({"Topic":"🏠 Overview","Level":"Start here","Core takeaway":"Review the pattern, meal, portions and personal needs.","Do ✅":"Make one sustainable meal change","Don't ⛔":"Chase a single perfect food","Myth versus fact 💡":"Myth: one meal determines health. Fact: repeated habits matter.","Key metric to follow 📏":"Variety and meal pattern","Suggested next step ➡️":"Choose one usual meal","Important context":"Cultural foods can fit.","Primary source":SOURCES["ICMR-NIN Indian guidelines"]})
    for title,do,dont,myth,metric,next_step,source in EXTRA:
        rows.append({"Topic":title,"Level":"Reference","Core takeaway":do,"Do ✅":do,"Don't ⛔":dont,"Myth versus fact 💡":myth,"Key metric to follow 📏":metric,"Suggested next step ➡️":next_step,"Important context":"Read the linked tab for details.","Primary source":SOURCES[source]})
    st.dataframe(rows,hide_index=True,use_container_width=True,height=570,column_config={"Primary source":st.column_config.LinkColumn("Primary source")})
    st.caption("Swipe or scroll the wide table horizontally. Select a topic tab above for its example, quiz and source notes.")
    st.subheader("📊 High-value official reference tables")
    st.write("These figures are copied as short summaries of official guidance; follow the linked source for scope and revisions.")
    st.dataframe([{"Authority":a,"Measure":m,"Reference":v,"How to use it":n,"Original chart or guidance":u} for a,m,v,n,u in REFERENCES],hide_index=True,use_container_width=True,column_config={"Original chart or guidance":st.column_config.LinkColumn("Original chart or guidance")})
    st.caption("WHO goals are broad population guidance. A clinician may set different targets for specific medical needs.")
    st.markdown(f"**🌡️ Food thermometer quick chart** · [Full government chart ↗]({SAFETY_URL})")
    st.dataframe([{"Food":food,"Minimum internal temperature":temp} for food,temp in SAFETY],hide_index=True,use_container_width=True)
    st.caption("Use a food thermometer; additional foods and exceptions are in the linked FoodSafety.gov chart.")
