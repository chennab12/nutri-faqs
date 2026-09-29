"""Editorial reading shortlist from public-health and clinical authorities.

Selection is based on relevance, evidence provenance, and practical utility;
'best 1%' is not a measured ranking. Links are maintained by their publishers.
"""
import streamlit as st
from content import SOURCES

NOTES = {
    "WHO healthy diet": ("🌍", "Healthy pattern and guardrails", "Use the overall balance of variety, vegetables and fruit, fats, sugars and salt to review a normal week."),
    "ICMR-NIN Indian guidelines": ("🇮🇳", "India-specific food patterns", "Use local food groups and familiar meals as the starting point; adapt portions to the person."),
    "AHA dietary guidance": ("❤️", "Heart-health choices", "Compare repeated fat sources, sodium and food quality across your whole pattern."),
    "ADA diabetes plate": ("🍽️", "A visual meal method", "Sketch non-starchy vegetables, protein foods and carbohydrate foods together; individualize for diabetes treatment."),
    "FDA added-sugar label": ("🏷️", "Read added sugar correctly", "Check serving size first, then multiply added-sugar grams by servings eaten."),
    "FoodSafety.gov four steps": ("🧼", "Prevent foodborne illness", "Check clean, separate, cook and chill each time you handle perishable foods."),
    "FDA food allergies": ("🥜", "Allergen labels and reactions", "Read every ingredient label and follow the diagnosed allergy and emergency plan."),
    "NIDDK GERD diet": ("🫖", "Reflux and meal timing", "Notice personal symptom triggers and timing; discuss persistent symptoms."),
    "NIH supplement basics": ("💊", "Supplement safety questions", "Check evidence, dose and medicine interactions before buying a product."),
    "NIH supplement library": ("🔬", "Nutrient fact sheets", "Look up the specific nutrient, intake guidance and upper limits before interpreting a claim."),
    "NCCIH Ayurveda": ("🌿", "Tradition, evidence and safety", "Separate ordinary culinary practices from therapeutic product claims and safety risks."),
    "NCCIH homeopathy": ("🧪", "Treatment claims under review", "Use evidence-based care for a health condition; a remedy claim does not establish benefit."),
    "NCCIH integrative health": ("🧭", "Terms and care coordination", "Clarify which practice is being proposed and discuss it alongside established care."),
}
EXTRA = {
    "MedlinePlus RSS directory": ("📰", "Official topic feeds", "Find a nutrition or health topic feed; a feed may be empty until new links are added.", "https://medlineplus.gov/rss.html"),
    "USDA FoodData Central": ("📊", "Food composition lookup", "Look up measured nutrients for a named food and check the specified serving quantity.", "https://fdc.nal.usda.gov/"),
}
PICKS = {
    "Overview": ["WHO healthy diet", "ICMR-NIN Indian guidelines", "MedlinePlus RSS directory"],
    "Kitchen tools": ["ADA diabetes plate", "FDA added-sugar label", "USDA FoodData Central"],
    "Sources": ["ICMR-NIN Indian guidelines", "WHO healthy diet", "MedlinePlus RSS directory"],
    "Compare approaches": ["WHO healthy diet", "NCCIH Ayurveda", "NCCIH homeopathy"],
    "Ayurveda in the kitchen": ["ICMR-NIN Indian guidelines", "NCCIH Ayurveda", "WHO healthy diet"],
    "Homeopathy and decision guide": ["NCCIH homeopathy", "NCCIH integrative health", "NIH supplement basics"],
}

def render(title, sources=None):
    """Show compact, actionable links for every output tab."""
    selected = PICKS.get(title, sources or [])[:3]
    st.subheader("🔎 Trusted reading: three useful next clicks" if len(selected) == 3 else "🔎 Trusted reading")
    st.caption("Editorial picks for this topic, not a numerical ranking or a live medical recommendation. Publisher pages may change.")
    columns = st.columns(len(selected))
    for col, name in zip(columns, selected):
        icon, purpose, action, url = EXTRA[name] if name in EXTRA else (*NOTES[name], SOURCES[name])
        with col:
            st.markdown(f"**{icon} {purpose}**")
            st.markdown(f"[{name} ↗]({url})")
            st.caption(action)
    with st.expander("📰 Follow new evidence-aware links"):
        st.write("MedlinePlus offers RSS feeds for individual health topics. Its feeds show newly added links, not an exhaustive or continuously updated evidence review; a topic feed can be empty.")
        st.markdown("[Browse official MedlinePlus topic feeds ↗](https://medlineplus.gov/rss.html)")
