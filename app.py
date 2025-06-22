import streamlit as st

st.title("Dermatophyte Clinical Simulation")

st.write("Welcome to your in-silico dermatophyte diagnostic tool!")
st.write("Choose a case from the sidebar to begin.")

cases = {
    "Case 1: Tinea Corporis (Ringworm of the Body)": {
        "history": "A 23-year-old male presents with an itchy, circular rash on his forearm. The lesion has raised, scaly edges and central clearing. He works at a daycare and recently adopted a stray cat.",
        "image_local": "tinea_corporis.jpg",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Ringworm_on_the_arm%2C_or_tinea_corporis_due_to_Trichophyton_mentagrophytes_PHIL_2938_lores.jpg",
        "options": ["Tinea corporis", "Psoriasis", "Atopic dermatitis", "Impetigo"],
        "answer": "Tinea corporis",
        "feedback": "Correct! Classic for tinea corporis: ring-shaped, scaly lesion, animal contact."
    },
    "Case 2: Tinea Capitis (Scalp Ringworm)": {
        "history": "A 7-year-old boy presents with patchy hair loss and scaling of the scalp. Some areas show black dots and mild inflammation. Several classmates also have similar complaints.",
        "image_local": "tinea_capitis.jpg",  # Add local filename if downloaded
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Teigne_tondante_enfant.jpg",
        "options": ["Alopecia areata", "Seborrheic dermatitis", "Tinea capitis", "Psoriasis"],
        "answer": "Tinea capitis",
        "feedback": "Correct! Patchy hair loss, scaling, and black dots (broken hairs) in a child, plus school outbreak, point to tinea capitis."
    },
    "Case 3: Tinea Pedis (Athlete’s Foot)": {
        "history": "A 28-year-old athlete complains of itchy, peeling skin between his toes. There is redness, scaling, and mild fissuring. He often uses communal showers at the gym.",
        "image_local": "tinea_pedis.jpg",
   	"image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Tinea_pedis_interdigitalis.jpg",
        "options": ["Tinea pedis", "Contact dermatitis", "Cellulitis", "Plantar warts"],
        "answer": "Tinea pedis",
        "feedback": "Correct! Interdigital scaling, itching, and exposure to communal showers suggest athlete’s foot (tinea pedis)."
    },
    "Case 4: Tinea Cruris (Jock Itch)": {
        "history": "A 35-year-old overweight man presents with a two-week history of an intensely itchy, red rash affecting his groin and inner thighs. The rash started as small patches and gradually expanded. On examination, the lesions are sharply demarcated, erythematous plaques with slightly raised, scaly borders and central clearing. The scrotum is spared. He reports increased sweating and tight clothing, especially during exercise. There is no history of recent antibiotic use, diabetes, or similar symptoms in sexual partners.",
	"image_local": "jock_itch.jpg",
	"image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Jock_itch_in_groin.jpg/4128px-Jock_itch_in_groin.jpg",
        "options": ["Candidal intertrigo", "Tinea cruris", "Psoriasis", "Lichen planus"],
        "answer": "Tinea cruris",
        "feedback": "Correct! Tinea cruris spares the scrotum, affects groin/thighs, and has sharply demarcated borders."
    },
"Case 5: Tinea Unguium (Onychomycosis)": {
    "history": "A 55-year-old woman presents with progressive thickening, yellow-brown discoloration, and crumbling of several toenails over the past year. She notes the nails are becoming increasingly brittle and difficult to trim. There is no significant pain, but she is concerned about their appearance. She has a long-standing history of athlete’s foot (tinea pedis) and reports wearing occlusive footwear for long hours. No history of recent trauma or psoriasis.",
    "image_local": "tinea_unguium.jpg",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Onychomycosis_due_to_Trichophyton_rubrum%2C_right_and_left_great_toe_PHIL_579_lores.jpg",
    "options": ["Psoriasis", "Onychomycosis (Tinea unguium)", "Trauma", "Paronychia"],
    "answer": "Onychomycosis (Tinea unguium)",
    "feedback": "Correct! Nail thickening, discoloration, and a history of athlete’s foot are classic for fungal nail infection."
    },
"Case 6: Tinea Barbae (Beard Area Ringworm)": {
    "history": "A 32-year-old male barber presents with several weeks of painful, inflamed nodules and pustules on his lower face and neck, mostly in the beard area. The lesions started as red papules and have progressed to boggy, tender swellings. He reports mild fever and difficulty shaving. No similar history in the past. No recent antibiotic use or trauma.",
    "image_local": "tinea_barbae.jpg",  # Save as this if you download it locally
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/22/Tinea_barbae_4807_lores.jpg",
    "options": [
        "Tinea barbae",
        "Acne vulgaris",
        "Bacterial folliculitis",
        "Discoid lupus erythematosus"
    ],
    "answer": "Tinea barbae",
    "feedback": "Correct! Deep, boggy, inflammatory plaques and nodules in the beard area, sometimes with pustules or hairs easily removed (hair epilation), are classic for tinea barbae—especially in those with animal contact or barbers."
    },
"Case 7: Tinea Manuum (Hand Ringworm)": {
    "history": (
        "A 45-year-old farmer presents with a chronic, dry, scaly rash involving the palm of his right hand. "
        "He reports mild itching and worsening roughness over several months. The rash does not improve with moisturizing creams. "
        "There is no involvement of the feet, but he reports a similar rash on his left foot a year ago. Examination shows diffuse scaling and erythema, mainly on the palm, with mild fissuring. No vesicles or pustules."
    ),
    "image_local": "tinea_manuum.jpg",  # Save as this locally if needed
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Tinea_manum.jpg",
    "options": [
        "Contact dermatitis",
        "Psoriasis",
        "Tinea manuum",
        "Hand eczema"
    ],
    "answer": "Tinea manuum",
    "feedback": "Correct! Unilateral, chronic scaling of the palm—often with a history of tinea pedis ('two feet-one hand' syndrome)—suggests tinea manuum. Moisturizers and steroids do not help."
    },
"Case 8: Tinea Versicolor (Pityriasis Versicolor)": {
    "history": (
        "A 38-year-old woman presents with gradually spreading light and brownish patches on her chest and upper back. "
        "She has noticed these areas are more prominent after sweating and during the summer months. Mild itching is present, but no pain. "
        "On examination, there are multiple, irregularly shaped, pale brown patches with very fine scaling. No history of similar complaints or chronic illnesses."
    ),
    "image_local": "tinea_versicolor.jpg",  # Save as this locally if needed
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/99/Tinea_versicolor_due_to_Malassezia_furfur_PHIL_2914_lores.jpg",
    "options": [
        "Tinea versicolor",
        "Vitiligo",
        "Pityriasis alba",
        "Nummular eczema"
    ],
    "answer": "Tinea versicolor",
    "feedback": (
        "Correct! Tinea versicolor (Malassezia furfur infection) causes hypo- or hyperpigmented patches with fine scale, especially on the trunk or chest—often seen in adults and may worsen with humidity or sweating."
    )
    },
"Case 9: Majocchi Granuloma": {
    "history": (
        "A patient presents with a persistent, scaly, inflammatory granulomatous lesion typically "
        "found on the forearm or leg. The lesion often follows trauma or topical steroid use and "
        "is caused by dermatophytes invading the hair follicle, leading to a deeper infection."
    ),
    "image_local": "Majocchi_granuloma.jpg",  # Save as this locally if needed
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Majocchi_granuloma_new_image_in_2019_%28cropped%29.jpg",
    "options": [
        "Tinea corporis",
        "Majocchi Granuloma",
        "Psoriasis",
        "Eczema"
    ],
    "answer": "Majocchi Granuloma",
    "feedback": "Correct! Majocchi granuloma is a deep dermatophyte infection characterized by inflammatory granulomatous lesions often triggered by trauma or steroid use."
    },
"Case 10: Tinea Incognito": {
    "history": "A child presents with a persistent, atypical rash on the forearm that initially resembled ringworm but has become diffuse, inflamed, and less well-defined. The lesion lacks the classic scaly, annular border of typical dermatophyte infections. This change occurred after the patient was treated with topical corticosteroids prescribed for presumed eczema or contact dermatitis. The use of steroids suppressed the inflammatory response, allowing the fungal infection to spread and alter its appearance, making diagnosis difficult. The rash is itchy and may be accompanied by mild erythema and occasional scaling.",
    "image_local": "Tinea_incognito.jpg",  # Save as this locally if needed
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Tinea_incognito.jpg",
    "options": ["Tinea corporis", "Contact dermatitis", "Tinea incognito", "Psoriasis"],
    "answer": "Tinea incognito",
    "feedback": "Correct! Tinea incognito results from inappropriate steroid use that alters the typical appearance of dermatophyte infections, often leading to misdiagnosis."
    }



}

case_name = st.sidebar.radio("Choose a case:", list(cases.keys()))
case = cases[case_name]

st.subheader(case_name)
st.write(case["history"])
st.image(case["image_url"], caption=case_name, use_container_width=True)  # updated parameter
user_answer = st.radio("What's your diagnosis?", case["options"])

if st.button("Submit Answer"):
    if user_answer == case["answer"]:
        st.success(case["feedback"])
    else:
        st.error(f"Incorrect. The correct answer is: {case['answer']}")
