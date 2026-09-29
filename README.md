# Food & Nutrition Compass

A Streamlit learning dashboard with 15 lessons ordered from basic food concepts through advanced meal planning and condition-specific decisions. Every lesson includes a concept table, kitchen example, knowledge check, a focused trusted-reading shortlist with a practical action, an official MedlinePlus topic-feed directory, and an animated chef cartoon. Kitchen tools estimate plate proportions, energy from macronutrients and label totals. The final three tabs compare evidence-based nutrition, Ayurveda-inspired food traditions and homeopathy accurately and practically.

The content is general education, reviewed on 29 September 2026. It does not diagnose or prescribe a diet. The app makes clear that conventional medicine and homeopathy are not cooking styles, and that homeopathy has no reliable evidence as treatment for health conditions. Some Ayurvedic preparations may pose contamination or interaction risks. Individual medical conditions require individualized advice.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

For Streamlit Community Cloud, use `app.py` as the entry point. No API key is required. The app uses editorial, static links and does not scrape or assert a measured “top 1%” ranking. MedlinePlus topic feeds may be empty between updates. Visuals are inline code-native SVG and switch to static under reduced-motion settings.
