"""Food & Nutrition Compass: progressive lessons and evidence-aware comparisons."""
import streamlit as st
from content import LESSONS, SOURCES
from visuals import show
from trusted_reading import render as trusted_reading
from master_cheatsheet import render as master_cheatsheet
from approaches import render as approaches_comparison

st.set_page_config(page_title="Food & Nutrition Compass",page_icon="🥗",layout="wide")
st.title("🥗 Food & Nutrition Compass")
st.caption("Basics → intermediate → advanced · Practical food choices · Sources reviewed 29 September 2026")
st.info("Educational guide for everyday meals. Individual needs differ with age, pregnancy, allergies, medications and medical conditions. A clinician or registered dietitian can tailor a treatment plan.")
LESSON_ICONS=["🌱","🍽️","⚡","💪","🌾","❤️","🔬","💧","🏷️","🧼","🥜","🍳","🛒","🩺","💊"]
names=["📌 Master cheatsheet","🏠 Overview"]+[f"{icon} {x['title']}" for icon,x in zip(LESSON_ICONS,LESSONS)]+["🧮 Kitchen tools","📚 Sources","⚖️ Compare approaches","🌿 Ayurveda in the kitchen","🧪 Homeopathy & decisions","🧭 Health approaches"]
tabs=st.tabs(names)

with tabs[0]:
    master_cheatsheet()

with tabs[1]:
    st.subheader("A useful food decision in four steps")
    st.write("Start with a varied pattern, build a satisfying meal, check portions and preparation, then adapt to your health needs. Familiar foods such as rice, dal, idli, vegetables, fruit and curd can all fit.")
    a,b,c=st.columns(3)
    a.metric("Curriculum","15 lessons")
    b.metric("Kitchen tools","3 quick tools")
    c.metric("Approach comparison","3 tabs")
    st.dataframe([{"Order":i,"Topic":x["title"],"Level":x["level"],"One-line takeaway":x["takeaway"]} for i,x in enumerate(LESSONS,1)],hide_index=True,use_container_width=True)
    st.markdown("**First action:** choose one ordinary meal and ask what it contains, what is missing, and whether any medical condition changes the choice.")
    trusted_reading("Overview")
    show("Overview")

for tab,lesson in zip(tabs[2:2+len(LESSONS)],LESSONS):
    with tab:
        st.header(lesson["title"])
        st.caption(lesson["level"]+" · "+lesson["takeaway"])
        st.subheader("Core concepts")
        st.dataframe([{"Concept":name,"Plain meaning":meaning,"Intuitive food example":example,"Practical takeaway":action} for name,meaning,example,action in lesson["concepts"]],hide_index=True,use_container_width=True)
        st.markdown("**Put it together:** "+lesson["example"])
        st.markdown("**Try this week:** "+lesson["action"])
        with st.expander("Knowledge check: "+lesson["question"]):
            st.text_area("Explain in your own words first",key="draft_"+lesson["title"],height=70)
            if st.checkbox("Reveal practical answer",key="reveal_"+lesson["title"]):st.success(lesson["answer"])
        st.markdown("**Original guidance:** "+" · ".join(f"[{name}]({SOURCES[name]})" for name in lesson["sources"]))
        st.caption("These examples are general education. Avoid changing prescribed treatment based on a meal example.")
        trusted_reading(lesson["title"],lesson["sources"])
        st.subheader("Animated memory cue")
        show(lesson["title"])

with tabs[-6]:
    st.header("🧮 Kitchen tools")
    st.write("Estimates make a meal easier to inspect. They do not prescribe a personal calorie or nutrient target.")
    tool=st.selectbox("Choose a tool",["Meal balance sketch","Macronutrient energy estimate","Package label portions"])
    if tool=="Meal balance sketch":
        vegetables=st.slider("Vegetables and fruit share (%)",0,100,50,5)
        protein=st.slider("Protein-food share (%)",0,100,25,5)
        grain=max(0,100-vegetables-protein)
        if vegetables+protein>100:st.warning("The two selected shares exceed 100%; reduce one.")
        else:
            st.bar_chart({"Illustrative plate share (%)":{"Vegetables/fruit":vegetables,"Protein foods":protein,"Grain/starch":grain}})
            st.caption("This sketch is a visual planning aid. Fruit can also be served on the side; adequacy and portions depend on the person.")
    elif tool=="Macronutrient energy estimate":
        carb=st.number_input("Carbohydrate (g)",0.0,1000.0,45.0)
        protein=st.number_input("Protein (g)",0.0,1000.0,15.0)
        fat=st.number_input("Fat (g)",0.0,1000.0,12.0)
        st.metric("Approx energy from these macros",f"{4*carb+4*protein+9*fat:.0f} kcal")
        st.caption("Uses 4 kcal/g for carbohydrate and protein, 9 kcal/g for fat. Actual labels can differ due to fiber, rounding and other ingredients.")
    else:
        servings=st.number_input("Servings eaten",0.0,20.0,2.0,0.5)
        sugar=st.number_input("Added sugar per serving (g)",0.0,200.0,8.0)
        sodium=st.number_input("Sodium per serving (mg)",0.0,5000.0,260.0)
        a,b=st.columns(2)
        a.metric("Total added sugar",f"{servings*sugar:g} g")
        b.metric("Total sodium",f"{servings*sodium:g} mg")
        st.caption("Serving-size multiplication is arithmetic, not a judgement that a product is safe for a particular condition.")
    st.markdown(f"[FDA label explanation]({SOURCES['FDA added-sugar label']}) · [WHO healthy-diet guidance]({SOURCES['WHO healthy diet']})")
    trusted_reading("Kitchen tools")
    show("Kitchen tools")

with tabs[-5]:
    st.header("📚 Sources and method")
    st.write("Primary public-health and clinical sources provide the medical and nutrition facts. Indian food examples are grounded in ICMR-NIN guidance. The site is a curated snapshot, not a live advice or diagnosis service.")
    st.dataframe([{"Source":name,"Direct link":url} for name,url in SOURCES.items()],hide_index=True,use_container_width=True,column_config={"Direct link":st.column_config.LinkColumn("Direct link")})
    st.markdown("**How to check a food claim:** identify the actual intervention, human outcome, study quality, possible harms, and whether the result applies to your own situation.")
    trusted_reading("Sources")
    show("Sources")

with tabs[-4]:
    st.header("⚖️ Conventional nutrition, Ayurveda and homeopathy")
    st.info("“Allopathy” is an informal label for conventional medicine; it is not a style of cooking. Homeopathy also has no distinct evidence-based cooking method. Compare the health claims and practices on their own merits.")
    st.dataframe([
        {"Approach":"Evidence-based nutrition within conventional care","Food or living focus":"Dietary patterns, portions, food safety and condition-specific plans","Evidence for health decisions":"Guidelines and clinical studies vary by question","When useful":"Default foundation; especially for diagnosed conditions","How to practice":"Use regular foods, monitor outcomes, coordinate with clinician/dietitian"},
        {"Approach":"Ayurveda-inspired food traditions","Food or living focus":"Culturally familiar meals, spices, timing and routines","Evidence for medical claims":"Varies; traditional theory alone does not establish clinical effectiveness","When useful":"For preference and sustainable routine if safe","How to practice":"Use ordinary wholesome foods; check claims and avoid risky products"},
        {"Approach":"Homeopathy","Food or living focus":"Remedy system, not a cooking or nutrition framework","Evidence for treating disease":"No reliable evidence of effectiveness for health conditions in major reviews","When useful":"Not a substitute for evidence-based nutrition or needed treatment","How to practice":"Do not delay diagnosis or treatment; discuss any products with clinician"},
    ],hide_index=True,use_container_width=True)
    st.markdown(f"[WHO nutrition]({SOURCES['WHO healthy diet']}) · [NCCIH Ayurveda]({SOURCES['NCCIH Ayurveda']}) · [NCCIH homeopathy]({SOURCES['NCCIH homeopathy']})")
    trusted_reading("Compare approaches")
    show("Compare approaches")

with tabs[-3]:
    st.header("🌿 Ayurveda in the kitchen")
    st.write("A traditional food routine can be enjoyable and easier to sustain. Judge a meal by ingredients, adequacy, portions, safety and how it fits the person's health needs. A spice or meal pattern is not, by itself, a treatment for diabetes, high cholesterol or another illness.")
    st.dataframe([
        {"Practice":"Warm cooked dal and vegetables","Potential value":"Familiar, satisfying way to include legumes and produce","Check":"Protein, portions and any individual restrictions"},
        {"Practice":"Use spices for flavor","Potential value":"May make meals enjoyable with less reliance on salt","Check":"Culinary use differs from concentrated herbal products"},
        {"Practice":"Regular meal routine","Potential value":"May support consistency","Check":"Adapt timing to work, medicines and symptoms"},
        {"Practice":"Herbal or mineral preparations","Potential value":"Specific benefit must be demonstrated","Check":"Interactions and contamination; some preparations contain heavy metals"},
    ],hide_index=True,use_container_width=True)
    st.markdown(f"[ICMR-NIN food guidance]({SOURCES['ICMR-NIN Indian guidelines']}) · [NCCIH safety and evidence]({SOURCES['NCCIH Ayurveda']})")
    st.caption("Do not discontinue prescribed treatment in favor of a dietary rule or preparation.")
    trusted_reading("Ayurveda in the kitchen")
    show("Ayurveda in the kitchen")

with tabs[-2]:
    st.header("🧪 Homeopathy and a practical decision guide")
    st.write("Homeopathy is a remedy system, not a cooking style. A healthy meal remains a healthy meal regardless of the label attached to it. Major evidence reviews have not found reliable evidence that homeopathy treats health conditions.")
    situation=st.selectbox("What is your decision?",["Everyday healthy meal","Documented nutrient deficiency","Diabetes, heart or kidney condition","Herbal or homeopathic product claim"])
    advice={
        "Everyday healthy meal":"Use varied foods and food-safety basics; traditional recipes can fit when the ingredients and portions work for you.",
        "Documented nutrient deficiency":"Discuss the result, cause and proven dose or treatment with a clinician; food alone may not correct it.",
        "Diabetes, heart or kidney condition":"Use a condition-specific plan from a clinician or dietitian; do not substitute a remedy for prescribed care.",
        "Herbal or homeopathic product claim":"Ask what controlled human evidence supports the exact claim, whether the product interacts with medicines, and whether care would be delayed.",
    }
    st.info(advice[situation])
    st.markdown(f"[NCCIH homeopathy evidence]({SOURCES['NCCIH homeopathy']}) · [NCCIH integrative-health definitions]({SOURCES['NCCIH integrative health']}) · [NIH supplement safety]({SOURCES['NIH supplement basics']})")
    trusted_reading("Homeopathy and decision guide")
    show("Homeopathy and decision guide")

with tabs[-1]:
    approaches_comparison()
