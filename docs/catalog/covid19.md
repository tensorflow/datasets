<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="covid19" />
  <meta itemprop="description" content="This repository attempts to assemble the largest Covid-19 epidemiological database&#10;in addition to a powerful set of expansive covariates. It includes open, publicly sourced,&#10;licensed data relating to demographics, economy, epidemiology, geography, health, hospitalizations,&#10;mobility, government response, weather, and more.&#10;&#10;This particular dataset corresponds to a join of all the different tables that are part of the repository.&#10;Therefore, expect the resulting samples to be highly sparse.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;covid19&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/covid19" />
  <meta itemprop="sameAs" content="https://github.com/GoogleCloudPlatform/covid-19-open-data" />
  <meta itemprop="citation" content="@article{Wahltinez2020,&#10;  author = &quot;O. Wahltinez and others&quot;,&#10;  year = 2020,&#10;  title = &quot;COVID-19 Open-Data: curating a fine-grained, global-scale data repository for SARS-CoV-2&quot;,&#10;  note = &quot;Work in progress&quot;,&#10;  url = {https://goo.gle/covid-19-open-data},&#10;}" />
</div>

# `covid19`


*   **Description**:

This repository attempts to assemble the largest Covid-19 epidemiological
database in addition to a powerful set of expansive covariates. It includes
open, publicly sourced, licensed data relating to demographics, economy,
epidemiology, geography, health, hospitalizations, mobility, government
response, weather, and more.

This particular dataset corresponds to a join of all the different tables that
are part of the repository. Therefore, expect the resulting samples to be highly
sparse.

*   **Homepage**:
    [https://github.com/GoogleCloudPlatform/covid-19-open-data](https://github.com/GoogleCloudPlatform/covid-19-open-data)

*   **Source code**:
    [`tfds.structured.covid19.Covid19`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/covid19/covid19.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `693.43 MiB`

*   **Dataset size**: `288.55 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 11,266,422

*   **Feature structure**:

```python
FeaturesDict({
    'adult_female_mortality_rate': float64,
    'adult_male_mortality_rate': float64,
    'age_bin_0': string,
    'age_bin_1': string,
    'age_bin_2': string,
    'age_bin_3': string,
    'age_bin_4': string,
    'age_bin_5': string,
    'age_bin_6': string,
    'age_bin_7': string,
    'age_bin_8': string,
    'age_bin_9': string,
    'aggregation_level': float64,
    'area_rural_sq_km': float64,
    'area_sq_km': float64,
    'area_urban_sq_km': float64,
    'average_temperature_celsius': float64,
    'cancel_public_events': float64,
    'comorbidity_mortality_rate': float64,
    'contact_tracing': float64,
    'country_code': string,
    'country_name': string,
    'cumulative_confirmed': float64,
    'cumulative_confirmed_age_0': float64,
    'cumulative_confirmed_age_1': float64,
    'cumulative_confirmed_age_2': float64,
    'cumulative_confirmed_age_3': float64,
    'cumulative_confirmed_age_4': float64,
    'cumulative_confirmed_age_5': float64,
    'cumulative_confirmed_age_6': float64,
    'cumulative_confirmed_age_7': float64,
    'cumulative_confirmed_age_8': float64,
    'cumulative_confirmed_age_9': float64,
    'cumulative_confirmed_female': float64,
    'cumulative_confirmed_male': float64,
    'cumulative_deceased': float64,
    'cumulative_deceased_age_0': float64,
    'cumulative_deceased_age_1': float64,
    'cumulative_deceased_age_2': float64,
    'cumulative_deceased_age_3': float64,
    'cumulative_deceased_age_4': float64,
    'cumulative_deceased_age_5': float64,
    'cumulative_deceased_age_6': float64,
    'cumulative_deceased_age_7': float64,
    'cumulative_deceased_age_8': float64,
    'cumulative_deceased_age_9': float64,
    'cumulative_deceased_female': float64,
    'cumulative_deceased_male': float64,
    'cumulative_hospitalized_patients': float64,
    'cumulative_hospitalized_patients_age_0': float64,
    'cumulative_hospitalized_patients_age_1': float64,
    'cumulative_hospitalized_patients_age_2': float64,
    'cumulative_hospitalized_patients_age_3': float64,
    'cumulative_hospitalized_patients_age_4': float64,
    'cumulative_hospitalized_patients_age_5': float64,
    'cumulative_hospitalized_patients_age_6': float64,
    'cumulative_hospitalized_patients_age_7': float64,
    'cumulative_hospitalized_patients_age_8': float64,
    'cumulative_hospitalized_patients_age_9': float64,
    'cumulative_hospitalized_patients_female': float64,
    'cumulative_hospitalized_patients_male': float64,
    'cumulative_intensive_care_patients': float64,
    'cumulative_intensive_care_patients_age_0': float64,
    'cumulative_intensive_care_patients_age_1': float64,
    'cumulative_intensive_care_patients_age_2': float64,
    'cumulative_intensive_care_patients_age_3': float64,
    'cumulative_intensive_care_patients_age_4': float64,
    'cumulative_intensive_care_patients_age_5': float64,
    'cumulative_intensive_care_patients_age_6': float64,
    'cumulative_intensive_care_patients_age_7': float64,
    'cumulative_intensive_care_patients_age_8': float64,
    'cumulative_intensive_care_patients_age_9': float64,
    'cumulative_intensive_care_patients_female': float64,
    'cumulative_intensive_care_patients_male': float64,
    'cumulative_persons_fully_vaccinated': float64,
    'cumulative_persons_fully_vaccinated_janssen': float64,
    'cumulative_persons_fully_vaccinated_moderna': float64,
    'cumulative_persons_fully_vaccinated_pfizer': float64,
    'cumulative_persons_vaccinated': float64,
    'cumulative_recovered': float64,
    'cumulative_recovered_age_0': float64,
    'cumulative_recovered_age_1': float64,
    'cumulative_recovered_age_2': float64,
    'cumulative_recovered_age_3': float64,
    'cumulative_recovered_age_4': float64,
    'cumulative_recovered_age_5': float64,
    'cumulative_recovered_age_6': float64,
    'cumulative_recovered_age_7': float64,
    'cumulative_recovered_age_8': float64,
    'cumulative_recovered_age_9': float64,
    'cumulative_recovered_female': float64,
    'cumulative_recovered_male': float64,
    'cumulative_tested': float64,
    'cumulative_tested_age_0': float64,
    'cumulative_tested_age_1': float64,
    'cumulative_tested_age_2': float64,
    'cumulative_tested_age_3': float64,
    'cumulative_tested_age_4': float64,
    'cumulative_tested_age_5': float64,
    'cumulative_tested_age_6': float64,
    'cumulative_tested_age_7': float64,
    'cumulative_tested_age_8': float64,
    'cumulative_tested_age_9': float64,
    'cumulative_tested_female': float64,
    'cumulative_tested_male': float64,
    'cumulative_vaccine_doses_administered': float64,
    'cumulative_vaccine_doses_administered_janssen': float64,
    'cumulative_vaccine_doses_administered_moderna': float64,
    'cumulative_vaccine_doses_administered_pfizer': float64,
    'cumulative_ventilator_patients': float64,
    'current_hospitalized_patients': float64,
    'current_intensive_care_patients': float64,
    'current_ventilator_patients': float64,
    'datacommons_id': string,
    'date': string,
    'debt_relief': float64,
    'dew_point': float64,
    'diabetes_prevalence': float64,
    'elevation_m': float64,
    'emergency_investment_in_healthcare': float64,
    'facial_coverings': float64,
    'fiscal_measures': float64,
    'gdp_per_capita_usd': float64,
    'gdp_usd': float64,
    'health_expenditure_usd': float64,
    'hospital_beds_per_1000': float64,
    'human_capital_index': float64,
    'human_development_index': float64,
    'income_support': float64,
    'infant_mortality_rate': float64,
    'international_support': float64,
    'international_travel_controls': float64,
    'investment_in_vaccines': float64,
    'iso_3166_1_alpha_2': string,
    'iso_3166_1_alpha_3': string,
    'latitude': float64,
    'life_expectancy': float64,
    'locality_code': string,
    'locality_name': string,
    'location_key': string,
    'longitude': float64,
    'maximum_temperature_celsius': float64,
    'minimum_temperature_celsius': float64,
    'mobility_grocery_and_pharmacy': float64,
    'mobility_parks': float64,
    'mobility_residential': float64,
    'mobility_retail_and_recreation': float64,
    'mobility_transit_stations': float64,
    'mobility_workplaces': float64,
    'new_confirmed': float64,
    'new_confirmed_age_0': float64,
    'new_confirmed_age_1': float64,
    'new_confirmed_age_2': float64,
    'new_confirmed_age_3': float64,
    'new_confirmed_age_4': float64,
    'new_confirmed_age_5': float64,
    'new_confirmed_age_6': float64,
    'new_confirmed_age_7': float64,
    'new_confirmed_age_8': float64,
    'new_confirmed_age_9': float64,
    'new_confirmed_female': float64,
    'new_confirmed_male': float64,
    'new_deceased': float64,
    'new_deceased_age_0': float64,
    'new_deceased_age_1': float64,
    'new_deceased_age_2': float64,
    'new_deceased_age_3': float64,
    'new_deceased_age_4': float64,
    'new_deceased_age_5': float64,
    'new_deceased_age_6': float64,
    'new_deceased_age_7': float64,
    'new_deceased_age_8': float64,
    'new_deceased_age_9': float64,
    'new_deceased_female': float64,
    'new_deceased_male': float64,
    'new_hospitalized_patients': float64,
    'new_hospitalized_patients_age_0': float64,
    'new_hospitalized_patients_age_1': float64,
    'new_hospitalized_patients_age_2': float64,
    'new_hospitalized_patients_age_3': float64,
    'new_hospitalized_patients_age_4': float64,
    'new_hospitalized_patients_age_5': float64,
    'new_hospitalized_patients_age_6': float64,
    'new_hospitalized_patients_age_7': float64,
    'new_hospitalized_patients_age_8': float64,
    'new_hospitalized_patients_age_9': float64,
    'new_hospitalized_patients_female': float64,
    'new_hospitalized_patients_male': float64,
    'new_intensive_care_patients': float64,
    'new_intensive_care_patients_age_0': float64,
    'new_intensive_care_patients_age_1': float64,
    'new_intensive_care_patients_age_2': float64,
    'new_intensive_care_patients_age_3': float64,
    'new_intensive_care_patients_age_4': float64,
    'new_intensive_care_patients_age_5': float64,
    'new_intensive_care_patients_age_6': float64,
    'new_intensive_care_patients_age_7': float64,
    'new_intensive_care_patients_age_8': float64,
    'new_intensive_care_patients_age_9': float64,
    'new_intensive_care_patients_female': float64,
    'new_intensive_care_patients_male': float64,
    'new_persons_fully_vaccinated': float64,
    'new_persons_fully_vaccinated_janssen': float64,
    'new_persons_fully_vaccinated_moderna': float64,
    'new_persons_fully_vaccinated_pfizer': float64,
    'new_persons_vaccinated': float64,
    'new_recovered': float64,
    'new_recovered_age_0': float64,
    'new_recovered_age_1': float64,
    'new_recovered_age_2': float64,
    'new_recovered_age_3': float64,
    'new_recovered_age_4': float64,
    'new_recovered_age_5': float64,
    'new_recovered_age_6': float64,
    'new_recovered_age_7': float64,
    'new_recovered_age_8': float64,
    'new_recovered_age_9': float64,
    'new_recovered_female': float64,
    'new_recovered_male': float64,
    'new_tested': float64,
    'new_tested_age_0': float64,
    'new_tested_age_1': float64,
    'new_tested_age_2': float64,
    'new_tested_age_3': float64,
    'new_tested_age_4': float64,
    'new_tested_age_5': float64,
    'new_tested_age_6': float64,
    'new_tested_age_7': float64,
    'new_tested_age_8': float64,
    'new_tested_age_9': float64,
    'new_tested_female': float64,
    'new_tested_male': float64,
    'new_vaccine_doses_administered': float64,
    'new_vaccine_doses_administered_janssen': float64,
    'new_vaccine_doses_administered_moderna': float64,
    'new_vaccine_doses_administered_pfizer': float64,
    'new_ventilator_patients': float64,
    'nurses_per_1000': float64,
    'openstreetmap_id': string,
    'out_of_pocket_health_expenditure_usd': float64,
    'physicians_per_1000': float64,
    'place_id': string,
    'pollution_mortality_rate': float64,
    'population': float64,
    'population_age_00_09': float64,
    'population_age_10_19': float64,
    'population_age_20_29': float64,
    'population_age_30_39': float64,
    'population_age_40_49': float64,
    'population_age_50_59': float64,
    'population_age_60_69': float64,
    'population_age_70_79': float64,
    'population_age_80_and_older': float64,
    'population_clustered': float64,
    'population_density': float64,
    'population_female': float64,
    'population_largest_city': float64,
    'population_male': float64,
    'population_rural': float64,
    'population_urban': float64,
    'public_information_campaigns': float64,
    'public_transport_closing': float64,
    'rainfall_mm': float64,
    'relative_humidity': float64,
    'restrictions_on_gatherings': float64,
    'restrictions_on_internal_movement': float64,
    'school_closing': float64,
    'search_trends_abdominal_obesity': float64,
    'search_trends_abdominal_pain': float64,
    'search_trends_acne': float64,
    'search_trends_actinic_keratosis': float64,
    'search_trends_acute_bronchitis': float64,
    'search_trends_adrenal_crisis': float64,
    'search_trends_ageusia': float64,
    'search_trends_alcoholism': float64,
    'search_trends_allergic_conjunctivitis': float64,
    'search_trends_allergy': float64,
    'search_trends_amblyopia': float64,
    'search_trends_amenorrhea': float64,
    'search_trends_amnesia': float64,
    'search_trends_anal_fissure': float64,
    'search_trends_anaphylaxis': float64,
    'search_trends_anemia': float64,
    'search_trends_angina_pectoris': float64,
    'search_trends_angioedema': float64,
    'search_trends_angular_cheilitis': float64,
    'search_trends_anosmia': float64,
    'search_trends_anxiety': float64,
    'search_trends_aphasia': float64,
    'search_trends_aphonia': float64,
    'search_trends_apnea': float64,
    'search_trends_arthralgia': float64,
    'search_trends_arthritis': float64,
    'search_trends_ascites': float64,
    'search_trends_asperger_syndrome': float64,
    'search_trends_asphyxia': float64,
    'search_trends_asthma': float64,
    'search_trends_astigmatism': float64,
    'search_trends_ataxia': float64,
    'search_trends_atheroma': float64,
    'search_trends_attention_deficit_hyperactivity_disorder': float64,
    'search_trends_auditory_hallucination': float64,
    'search_trends_autoimmune_disease': float64,
    'search_trends_avoidant_personality_disorder': float64,
    'search_trends_back_pain': float64,
    'search_trends_bacterial_vaginosis': float64,
    'search_trends_balance_disorder': float64,
    'search_trends_beaus_lines': float64,
    'search_trends_bells_palsy': float64,
    'search_trends_biliary_colic': float64,
    'search_trends_binge_eating': float64,
    'search_trends_bleeding': float64,
    'search_trends_bleeding_on_probing': float64,
    'search_trends_blepharospasm': float64,
    'search_trends_bloating': float64,
    'search_trends_blood_in_stool': float64,
    'search_trends_blurred_vision': float64,
    'search_trends_blushing': float64,
    'search_trends_boil': float64,
    'search_trends_bone_fracture': float64,
    'search_trends_bone_tumor': float64,
    'search_trends_bowel_obstruction': float64,
    'search_trends_bradycardia': float64,
    'search_trends_braxton_hicks_contractions': float64,
    'search_trends_breakthrough_bleeding': float64,
    'search_trends_breast_pain': float64,
    'search_trends_bronchitis': float64,
    'search_trends_bruise': float64,
    'search_trends_bruxism': float64,
    'search_trends_bunion': float64,
    'search_trends_burn': float64,
    'search_trends_burning_chest_pain': float64,
    'search_trends_burning_mouth_syndrome': float64,
    'search_trends_candidiasis': float64,
    'search_trends_canker_sore': float64,
    'search_trends_cardiac_arrest': float64,
    'search_trends_carpal_tunnel_syndrome': float64,
    'search_trends_cataplexy': float64,
    'search_trends_cataract': float64,
    'search_trends_chancre': float64,
    'search_trends_cheilitis': float64,
    'search_trends_chest_pain': float64,
    'search_trends_chills': float64,
    'search_trends_chorea': float64,
    'search_trends_chronic_pain': float64,
    'search_trends_cirrhosis': float64,
    'search_trends_cleft_lip_and_cleft_palate': float64,
    'search_trends_clouding_of_consciousness': float64,
    'search_trends_cluster_headache': float64,
    'search_trends_colitis': float64,
    'search_trends_coma': float64,
    'search_trends_common_cold': float64,
    'search_trends_compulsive_behavior': float64,
    'search_trends_compulsive_hoarding': float64,
    'search_trends_confusion': float64,
    'search_trends_congenital_heart_defect': float64,
    'search_trends_conjunctivitis': float64,
    'search_trends_constipation': float64,
    'search_trends_convulsion': float64,
    'search_trends_cough': float64,
    'search_trends_crackles': float64,
    'search_trends_cramp': float64,
    'search_trends_crepitus': float64,
    'search_trends_croup': float64,
    'search_trends_cyanosis': float64,
    'search_trends_dandruff': float64,
    'search_trends_delayed_onset_muscle_soreness': float64,
    'search_trends_dementia': float64,
    'search_trends_dentin_hypersensitivity': float64,
    'search_trends_depersonalization': float64,
    'search_trends_depression': float64,
    'search_trends_dermatitis': float64,
    'search_trends_desquamation': float64,
    'search_trends_developmental_disability': float64,
    'search_trends_diabetes': float64,
    'search_trends_diabetic_ketoacidosis': float64,
    'search_trends_diarrhea': float64,
    'search_trends_dizziness': float64,
    'search_trends_dry_eye_syndrome': float64,
    'search_trends_dysautonomia': float64,
    'search_trends_dysgeusia': float64,
    'search_trends_dysmenorrhea': float64,
    'search_trends_dyspareunia': float64,
    'search_trends_dysphagia': float64,
    'search_trends_dysphoria': float64,
    'search_trends_dystonia': float64,
    'search_trends_dysuria': float64,
    'search_trends_ear_pain': float64,
    'search_trends_eczema': float64,
    'search_trends_edema': float64,
    'search_trends_encephalitis': float64,
    'search_trends_encephalopathy': float64,
    'search_trends_epidermoid_cyst': float64,
    'search_trends_epilepsy': float64,
    'search_trends_epiphora': float64,
    'search_trends_erectile_dysfunction': float64,
    'search_trends_erythema': float64,
    'search_trends_erythema_chronicum_migrans': float64,
    'search_trends_esophagitis': float64,
    'search_trends_excessive_daytime_sleepiness': float64,
    'search_trends_eye_pain': float64,
    'search_trends_eye_strain': float64,
    'search_trends_facial_nerve_paralysis': float64,
    'search_trends_facial_swelling': float64,
    'search_trends_fasciculation': float64,
    'search_trends_fatigue': float64,
    'search_trends_fatty_liver_disease': float64,
    'search_trends_fecal_incontinence': float64,
    'search_trends_fever': float64,
    'search_trends_fibrillation': float64,
    'search_trends_fibrocystic_breast_changes': float64,
    'search_trends_fibromyalgia': float64,
    'search_trends_flatulence': float64,
    'search_trends_floater': float64,
    'search_trends_focal_seizure': float64,
    'search_trends_folate_deficiency': float64,
    'search_trends_food_craving': float64,
    'search_trends_food_intolerance': float64,
    'search_trends_frequent_urination': float64,
    'search_trends_gastroesophageal_reflux_disease': float64,
    'search_trends_gastroparesis': float64,
    'search_trends_generalized_anxiety_disorder': float64,
    'search_trends_genital_wart': float64,
    'search_trends_gingival_recession': float64,
    'search_trends_gingivitis': float64,
    'search_trends_globus_pharyngis': float64,
    'search_trends_goitre': float64,
    'search_trends_gout': float64,
    'search_trends_grandiosity': float64,
    'search_trends_granuloma': float64,
    'search_trends_guilt': float64,
    'search_trends_hair_loss': float64,
    'search_trends_halitosis': float64,
    'search_trends_hay_fever': float64,
    'search_trends_headache': float64,
    'search_trends_heart_arrhythmia': float64,
    'search_trends_heart_murmur': float64,
    'search_trends_heartburn': float64,
    'search_trends_hematochezia': float64,
    'search_trends_hematoma': float64,
    'search_trends_hematuria': float64,
    'search_trends_hemolysis': float64,
    'search_trends_hemoptysis': float64,
    'search_trends_hemorrhoids': float64,
    'search_trends_hepatic_encephalopathy': float64,
    'search_trends_hepatitis': float64,
    'search_trends_hepatotoxicity': float64,
    'search_trends_hiccup': float64,
    'search_trends_hip_pain': float64,
    'search_trends_hives': float64,
    'search_trends_hot_flash': float64,
    'search_trends_hydrocephalus': float64,
    'search_trends_hypercalcaemia': float64,
    'search_trends_hypercapnia': float64,
    'search_trends_hypercholesterolemia': float64,
    'search_trends_hyperemesis_gravidarum': float64,
    'search_trends_hyperglycemia': float64,
    'search_trends_hyperhidrosis': float64,
    'search_trends_hyperkalemia': float64,
    'search_trends_hyperlipidemia': float64,
    'search_trends_hypermobility': float64,
    'search_trends_hyperpigmentation': float64,
    'search_trends_hypersomnia': float64,
    'search_trends_hypertension': float64,
    'search_trends_hyperthermia': float64,
    'search_trends_hyperthyroidism': float64,
    'search_trends_hypertriglyceridemia': float64,
    'search_trends_hypertrophy': float64,
    'search_trends_hyperventilation': float64,
    'search_trends_hypocalcaemia': float64,
    'search_trends_hypochondriasis': float64,
    'search_trends_hypoglycemia': float64,
    'search_trends_hypogonadism': float64,
    'search_trends_hypokalemia': float64,
    'search_trends_hypomania': float64,
    'search_trends_hyponatremia': float64,
    'search_trends_hypotension': float64,
    'search_trends_hypothyroidism': float64,
    'search_trends_hypoxemia': float64,
    'search_trends_hypoxia': float64,
    'search_trends_impetigo': float64,
    'search_trends_implantation_bleeding': float64,
    'search_trends_impulsivity': float64,
    'search_trends_indigestion': float64,
    'search_trends_infection': float64,
    'search_trends_inflammation': float64,
    'search_trends_inflammatory_bowel_disease': float64,
    'search_trends_ingrown_hair': float64,
    'search_trends_insomnia': float64,
    'search_trends_insulin_resistance': float64,
    'search_trends_intermenstrual_bleeding': float64,
    'search_trends_intracranial_pressure': float64,
    'search_trends_iron_deficiency': float64,
    'search_trends_irregular_menstruation': float64,
    'search_trends_itch': float64,
    'search_trends_jaundice': float64,
    'search_trends_kidney_failure': float64,
    'search_trends_kidney_stone': float64,
    'search_trends_knee_pain': float64,
    'search_trends_kyphosis': float64,
    'search_trends_lactose_intolerance': float64,
    'search_trends_laryngitis': float64,
    'search_trends_leg_cramps': float64,
    'search_trends_lesion': float64,
    'search_trends_leukorrhea': float64,
    'search_trends_lightheadedness': float64,
    'search_trends_low_back_pain': float64,
    'search_trends_low_grade_fever': float64,
    'search_trends_lymphedema': float64,
    'search_trends_major_depressive_disorder': float64,
    'search_trends_malabsorption': float64,
    'search_trends_male_infertility': float64,
    'search_trends_manic_disorder': float64,
    'search_trends_melasma': float64,
    'search_trends_melena': float64,
    'search_trends_meningitis': float64,
    'search_trends_menorrhagia': float64,
    'search_trends_middle_back_pain': float64,
    'search_trends_migraine': float64,
    'search_trends_milium': float64,
    'search_trends_mitral_insufficiency': float64,
    'search_trends_mood_disorder': float64,
    'search_trends_mood_swing': float64,
    'search_trends_morning_sickness': float64,
    'search_trends_motion_sickness': float64,
    'search_trends_mouth_ulcer': float64,
    'search_trends_muscle_atrophy': float64,
    'search_trends_muscle_weakness': float64,
    'search_trends_myalgia': float64,
    'search_trends_mydriasis': float64,
    'search_trends_myocardial_infarction': float64,
    'search_trends_myoclonus': float64,
    'search_trends_nasal_congestion': float64,
    'search_trends_nasal_polyp': float64,
    'search_trends_nausea': float64,
    'search_trends_neck_mass': float64,
    'search_trends_neck_pain': float64,
    'search_trends_neonatal_jaundice': float64,
    'search_trends_nerve_injury': float64,
    'search_trends_neuralgia': float64,
    'search_trends_neutropenia': float64,
    'search_trends_night_sweats': float64,
    'search_trends_night_terror': float64,
    'search_trends_nocturnal_enuresis': float64,
    'search_trends_nodule': float64,
    'search_trends_nosebleed': float64,
    'search_trends_nystagmus': float64,
    'search_trends_obesity': float64,
    'search_trends_onychorrhexis': float64,
    'search_trends_oral_candidiasis': float64,
    'search_trends_orthostatic_hypotension': float64,
    'search_trends_osteopenia': float64,
    'search_trends_osteophyte': float64,
    'search_trends_osteoporosis': float64,
    'search_trends_otitis': float64,
    'search_trends_otitis_externa': float64,
    'search_trends_otitis_media': float64,
    'search_trends_pain': float64,
    'search_trends_palpitations': float64,
    'search_trends_pancreatitis': float64,
    'search_trends_panic_attack': float64,
    'search_trends_papule': float64,
    'search_trends_paranoia': float64,
    'search_trends_paresthesia': float64,
    'search_trends_pelvic_inflammatory_disease': float64,
    'search_trends_pericarditis': float64,
    'search_trends_periodontal_disease': float64,
    'search_trends_periorbital_puffiness': float64,
    'search_trends_peripheral_neuropathy': float64,
    'search_trends_perspiration': float64,
    'search_trends_petechia': float64,
    'search_trends_phlegm': float64,
    'search_trends_photodermatitis': float64,
    'search_trends_photophobia': float64,
    'search_trends_photopsia': float64,
    'search_trends_pleural_effusion': float64,
    'search_trends_pleurisy': float64,
    'search_trends_pneumonia': float64,
    'search_trends_podalgia': float64,
    'search_trends_polycythemia': float64,
    'search_trends_polydipsia': float64,
    'search_trends_polyneuropathy': float64,
    'search_trends_polyuria': float64,
    'search_trends_poor_posture': float64,
    'search_trends_post_nasal_drip': float64,
    'search_trends_postural_orthostatic_tachycardia_syndrome': float64,
    'search_trends_prediabetes': float64,
    'search_trends_proteinuria': float64,
    'search_trends_pruritus_ani': float64,
    'search_trends_psychosis': float64,
    'search_trends_ptosis': float64,
    'search_trends_pulmonary_edema': float64,
    'search_trends_pulmonary_hypertension': float64,
    'search_trends_purpura': float64,
    'search_trends_pus': float64,
    'search_trends_pyelonephritis': float64,
    'search_trends_radiculopathy': float64,
    'search_trends_rectal_pain': float64,
    'search_trends_rectal_prolapse': float64,
    'search_trends_red_eye': float64,
    'search_trends_renal_colic': float64,
    'search_trends_restless_legs_syndrome': float64,
    'search_trends_rheum': float64,
    'search_trends_rhinitis': float64,
    'search_trends_rhinorrhea': float64,
    'search_trends_rosacea': float64,
    'search_trends_round_ligament_pain': float64,
    'search_trends_rumination': float64,
    'search_trends_scar': float64,
    'search_trends_sciatica': float64,
    'search_trends_scoliosis': float64,
    'search_trends_seborrheic_dermatitis': float64,
    'search_trends_self_harm': float64,
    'search_trends_sensitivity_to_sound': float64,
    'search_trends_sexual_dysfunction': float64,
    'search_trends_shallow_breathing': float64,
    'search_trends_sharp_pain': float64,
    'search_trends_shivering': float64,
    'search_trends_shortness_of_breath': float64,
    'search_trends_shyness': float64,
    'search_trends_sinusitis': float64,
    'search_trends_skin_condition': float64,
    'search_trends_skin_rash': float64,
    'search_trends_skin_tag': float64,
    'search_trends_skin_ulcer': float64,
    'search_trends_sleep_apnea': float64,
    'search_trends_sleep_deprivation': float64,
    'search_trends_sleep_disorder': float64,
    'search_trends_snoring': float64,
    'search_trends_sore_throat': float64,
    'search_trends_spasticity': float64,
    'search_trends_splenomegaly': float64,
    'search_trends_sputum': float64,
    'search_trends_stomach_rumble': float64,
    'search_trends_strabismus': float64,
    'search_trends_stretch_marks': float64,
    'search_trends_stridor': float64,
    'search_trends_stroke': float64,
    'search_trends_stuttering': float64,
    'search_trends_subdural_hematoma': float64,
    'search_trends_suicidal_ideation': float64,
    'search_trends_swelling': float64,
    'search_trends_swollen_feet': float64,
    'search_trends_swollen_lymph_nodes': float64,
    'search_trends_syncope': float64,
    'search_trends_tachycardia': float64,
    'search_trends_tachypnea': float64,
    'search_trends_telangiectasia': float64,
    'search_trends_tenderness': float64,
    'search_trends_testicular_pain': float64,
    'search_trends_throat_irritation': float64,
    'search_trends_thrombocytopenia': float64,
    'search_trends_thyroid_nodule': float64,
    'search_trends_tic': float64,
    'search_trends_tinnitus': float64,
    'search_trends_tonsillitis': float64,
    'search_trends_toothache': float64,
    'search_trends_tremor': float64,
    'search_trends_trichoptilosis': float64,
    'search_trends_tumor': float64,
    'search_trends_type_2_diabetes': float64,
    'search_trends_unconsciousness': float64,
    'search_trends_underweight': float64,
    'search_trends_upper_respiratory_tract_infection': float64,
    'search_trends_urethritis': float64,
    'search_trends_urinary_incontinence': float64,
    'search_trends_urinary_tract_infection': float64,
    'search_trends_urinary_urgency': float64,
    'search_trends_uterine_contraction': float64,
    'search_trends_vaginal_bleeding': float64,
    'search_trends_vaginal_discharge': float64,
    'search_trends_vaginitis': float64,
    'search_trends_varicose_veins': float64,
    'search_trends_vasculitis': float64,
    'search_trends_ventricular_fibrillation': float64,
    'search_trends_ventricular_tachycardia': float64,
    'search_trends_vertigo': float64,
    'search_trends_viral_pneumonia': float64,
    'search_trends_visual_acuity': float64,
    'search_trends_vomiting': float64,
    'search_trends_wart': float64,
    'search_trends_water_retention': float64,
    'search_trends_weakness': float64,
    'search_trends_weight_gain': float64,
    'search_trends_wheeze': float64,
    'search_trends_xeroderma': float64,
    'search_trends_xerostomia': float64,
    'search_trends_yawn': float64,
    'smoking_prevalence': float64,
    'snowfall_mm': float64,
    'stay_at_home_requirements': float64,
    'stringency_index': float64,
    'subregion1_code': string,
    'subregion1_name': string,
    'subregion2_code': string,
    'subregion2_name': string,
    'testing_policy': float64,
    'vaccination_policy': float64,
    'wikidata_id': string,
    'workplace_closing': float64,
})
```

*   **Feature documentation**:

Feature                                                 | Class        | Shape | Dtype   | Description
:------------------------------------------------------ | :----------- | :---- | :------ | :----------
                                                        | FeaturesDict |       |         |
adult_female_mortality_rate                             | Tensor       |       | float64 |
adult_male_mortality_rate                               | Tensor       |       | float64 |
age_bin_0                                               | Tensor       |       | string  |
age_bin_1                                               | Tensor       |       | string  |
age_bin_2                                               | Tensor       |       | string  |
age_bin_3                                               | Tensor       |       | string  |
age_bin_4                                               | Tensor       |       | string  |
age_bin_5                                               | Tensor       |       | string  |
age_bin_6                                               | Tensor       |       | string  |
age_bin_7                                               | Tensor       |       | string  |
age_bin_8                                               | Tensor       |       | string  |
age_bin_9                                               | Tensor       |       | string  |
aggregation_level                                       | Tensor       |       | float64 |
area_rural_sq_km                                        | Tensor       |       | float64 |
area_sq_km                                              | Tensor       |       | float64 |
area_urban_sq_km                                        | Tensor       |       | float64 |
average_temperature_celsius                             | Tensor       |       | float64 |
cancel_public_events                                    | Tensor       |       | float64 |
comorbidity_mortality_rate                              | Tensor       |       | float64 |
contact_tracing                                         | Tensor       |       | float64 |
country_code                                            | Tensor       |       | string  |
country_name                                            | Tensor       |       | string  |
cumulative_confirmed                                    | Tensor       |       | float64 |
cumulative_confirmed_age_0                              | Tensor       |       | float64 |
cumulative_confirmed_age_1                              | Tensor       |       | float64 |
cumulative_confirmed_age_2                              | Tensor       |       | float64 |
cumulative_confirmed_age_3                              | Tensor       |       | float64 |
cumulative_confirmed_age_4                              | Tensor       |       | float64 |
cumulative_confirmed_age_5                              | Tensor       |       | float64 |
cumulative_confirmed_age_6                              | Tensor       |       | float64 |
cumulative_confirmed_age_7                              | Tensor       |       | float64 |
cumulative_confirmed_age_8                              | Tensor       |       | float64 |
cumulative_confirmed_age_9                              | Tensor       |       | float64 |
cumulative_confirmed_female                             | Tensor       |       | float64 |
cumulative_confirmed_male                               | Tensor       |       | float64 |
cumulative_deceased                                     | Tensor       |       | float64 |
cumulative_deceased_age_0                               | Tensor       |       | float64 |
cumulative_deceased_age_1                               | Tensor       |       | float64 |
cumulative_deceased_age_2                               | Tensor       |       | float64 |
cumulative_deceased_age_3                               | Tensor       |       | float64 |
cumulative_deceased_age_4                               | Tensor       |       | float64 |
cumulative_deceased_age_5                               | Tensor       |       | float64 |
cumulative_deceased_age_6                               | Tensor       |       | float64 |
cumulative_deceased_age_7                               | Tensor       |       | float64 |
cumulative_deceased_age_8                               | Tensor       |       | float64 |
cumulative_deceased_age_9                               | Tensor       |       | float64 |
cumulative_deceased_female                              | Tensor       |       | float64 |
cumulative_deceased_male                                | Tensor       |       | float64 |
cumulative_hospitalized_patients                        | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_0                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_1                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_2                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_3                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_4                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_5                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_6                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_7                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_8                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_age_9                  | Tensor       |       | float64 |
cumulative_hospitalized_patients_female                 | Tensor       |       | float64 |
cumulative_hospitalized_patients_male                   | Tensor       |       | float64 |
cumulative_intensive_care_patients                      | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_0                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_1                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_2                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_3                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_4                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_5                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_6                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_7                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_8                | Tensor       |       | float64 |
cumulative_intensive_care_patients_age_9                | Tensor       |       | float64 |
cumulative_intensive_care_patients_female               | Tensor       |       | float64 |
cumulative_intensive_care_patients_male                 | Tensor       |       | float64 |
cumulative_persons_fully_vaccinated                     | Tensor       |       | float64 |
cumulative_persons_fully_vaccinated_janssen             | Tensor       |       | float64 |
cumulative_persons_fully_vaccinated_moderna             | Tensor       |       | float64 |
cumulative_persons_fully_vaccinated_pfizer              | Tensor       |       | float64 |
cumulative_persons_vaccinated                           | Tensor       |       | float64 |
cumulative_recovered                                    | Tensor       |       | float64 |
cumulative_recovered_age_0                              | Tensor       |       | float64 |
cumulative_recovered_age_1                              | Tensor       |       | float64 |
cumulative_recovered_age_2                              | Tensor       |       | float64 |
cumulative_recovered_age_3                              | Tensor       |       | float64 |
cumulative_recovered_age_4                              | Tensor       |       | float64 |
cumulative_recovered_age_5                              | Tensor       |       | float64 |
cumulative_recovered_age_6                              | Tensor       |       | float64 |
cumulative_recovered_age_7                              | Tensor       |       | float64 |
cumulative_recovered_age_8                              | Tensor       |       | float64 |
cumulative_recovered_age_9                              | Tensor       |       | float64 |
cumulative_recovered_female                             | Tensor       |       | float64 |
cumulative_recovered_male                               | Tensor       |       | float64 |
cumulative_tested                                       | Tensor       |       | float64 |
cumulative_tested_age_0                                 | Tensor       |       | float64 |
cumulative_tested_age_1                                 | Tensor       |       | float64 |
cumulative_tested_age_2                                 | Tensor       |       | float64 |
cumulative_tested_age_3                                 | Tensor       |       | float64 |
cumulative_tested_age_4                                 | Tensor       |       | float64 |
cumulative_tested_age_5                                 | Tensor       |       | float64 |
cumulative_tested_age_6                                 | Tensor       |       | float64 |
cumulative_tested_age_7                                 | Tensor       |       | float64 |
cumulative_tested_age_8                                 | Tensor       |       | float64 |
cumulative_tested_age_9                                 | Tensor       |       | float64 |
cumulative_tested_female                                | Tensor       |       | float64 |
cumulative_tested_male                                  | Tensor       |       | float64 |
cumulative_vaccine_doses_administered                   | Tensor       |       | float64 |
cumulative_vaccine_doses_administered_janssen           | Tensor       |       | float64 |
cumulative_vaccine_doses_administered_moderna           | Tensor       |       | float64 |
cumulative_vaccine_doses_administered_pfizer            | Tensor       |       | float64 |
cumulative_ventilator_patients                          | Tensor       |       | float64 |
current_hospitalized_patients                           | Tensor       |       | float64 |
current_intensive_care_patients                         | Tensor       |       | float64 |
current_ventilator_patients                             | Tensor       |       | float64 |
datacommons_id                                          | Tensor       |       | string  |
date                                                    | Tensor       |       | string  |
debt_relief                                             | Tensor       |       | float64 |
dew_point                                               | Tensor       |       | float64 |
diabetes_prevalence                                     | Tensor       |       | float64 |
elevation_m                                             | Tensor       |       | float64 |
emergency_investment_in_healthcare                      | Tensor       |       | float64 |
facial_coverings                                        | Tensor       |       | float64 |
fiscal_measures                                         | Tensor       |       | float64 |
gdp_per_capita_usd                                      | Tensor       |       | float64 |
gdp_usd                                                 | Tensor       |       | float64 |
health_expenditure_usd                                  | Tensor       |       | float64 |
hospital_beds_per_1000                                  | Tensor       |       | float64 |
human_capital_index                                     | Tensor       |       | float64 |
human_development_index                                 | Tensor       |       | float64 |
income_support                                          | Tensor       |       | float64 |
infant_mortality_rate                                   | Tensor       |       | float64 |
international_support                                   | Tensor       |       | float64 |
international_travel_controls                           | Tensor       |       | float64 |
investment_in_vaccines                                  | Tensor       |       | float64 |
iso_3166_1_alpha_2                                      | Tensor       |       | string  |
iso_3166_1_alpha_3                                      | Tensor       |       | string  |
latitude                                                | Tensor       |       | float64 |
life_expectancy                                         | Tensor       |       | float64 |
locality_code                                           | Tensor       |       | string  |
locality_name                                           | Tensor       |       | string  |
location_key                                            | Tensor       |       | string  |
longitude                                               | Tensor       |       | float64 |
maximum_temperature_celsius                             | Tensor       |       | float64 |
minimum_temperature_celsius                             | Tensor       |       | float64 |
mobility_grocery_and_pharmacy                           | Tensor       |       | float64 |
mobility_parks                                          | Tensor       |       | float64 |
mobility_residential                                    | Tensor       |       | float64 |
mobility_retail_and_recreation                          | Tensor       |       | float64 |
mobility_transit_stations                               | Tensor       |       | float64 |
mobility_workplaces                                     | Tensor       |       | float64 |
new_confirmed                                           | Tensor       |       | float64 |
new_confirmed_age_0                                     | Tensor       |       | float64 |
new_confirmed_age_1                                     | Tensor       |       | float64 |
new_confirmed_age_2                                     | Tensor       |       | float64 |
new_confirmed_age_3                                     | Tensor       |       | float64 |
new_confirmed_age_4                                     | Tensor       |       | float64 |
new_confirmed_age_5                                     | Tensor       |       | float64 |
new_confirmed_age_6                                     | Tensor       |       | float64 |
new_confirmed_age_7                                     | Tensor       |       | float64 |
new_confirmed_age_8                                     | Tensor       |       | float64 |
new_confirmed_age_9                                     | Tensor       |       | float64 |
new_confirmed_female                                    | Tensor       |       | float64 |
new_confirmed_male                                      | Tensor       |       | float64 |
new_deceased                                            | Tensor       |       | float64 |
new_deceased_age_0                                      | Tensor       |       | float64 |
new_deceased_age_1                                      | Tensor       |       | float64 |
new_deceased_age_2                                      | Tensor       |       | float64 |
new_deceased_age_3                                      | Tensor       |       | float64 |
new_deceased_age_4                                      | Tensor       |       | float64 |
new_deceased_age_5                                      | Tensor       |       | float64 |
new_deceased_age_6                                      | Tensor       |       | float64 |
new_deceased_age_7                                      | Tensor       |       | float64 |
new_deceased_age_8                                      | Tensor       |       | float64 |
new_deceased_age_9                                      | Tensor       |       | float64 |
new_deceased_female                                     | Tensor       |       | float64 |
new_deceased_male                                       | Tensor       |       | float64 |
new_hospitalized_patients                               | Tensor       |       | float64 |
new_hospitalized_patients_age_0                         | Tensor       |       | float64 |
new_hospitalized_patients_age_1                         | Tensor       |       | float64 |
new_hospitalized_patients_age_2                         | Tensor       |       | float64 |
new_hospitalized_patients_age_3                         | Tensor       |       | float64 |
new_hospitalized_patients_age_4                         | Tensor       |       | float64 |
new_hospitalized_patients_age_5                         | Tensor       |       | float64 |
new_hospitalized_patients_age_6                         | Tensor       |       | float64 |
new_hospitalized_patients_age_7                         | Tensor       |       | float64 |
new_hospitalized_patients_age_8                         | Tensor       |       | float64 |
new_hospitalized_patients_age_9                         | Tensor       |       | float64 |
new_hospitalized_patients_female                        | Tensor       |       | float64 |
new_hospitalized_patients_male                          | Tensor       |       | float64 |
new_intensive_care_patients                             | Tensor       |       | float64 |
new_intensive_care_patients_age_0                       | Tensor       |       | float64 |
new_intensive_care_patients_age_1                       | Tensor       |       | float64 |
new_intensive_care_patients_age_2                       | Tensor       |       | float64 |
new_intensive_care_patients_age_3                       | Tensor       |       | float64 |
new_intensive_care_patients_age_4                       | Tensor       |       | float64 |
new_intensive_care_patients_age_5                       | Tensor       |       | float64 |
new_intensive_care_patients_age_6                       | Tensor       |       | float64 |
new_intensive_care_patients_age_7                       | Tensor       |       | float64 |
new_intensive_care_patients_age_8                       | Tensor       |       | float64 |
new_intensive_care_patients_age_9                       | Tensor       |       | float64 |
new_intensive_care_patients_female                      | Tensor       |       | float64 |
new_intensive_care_patients_male                        | Tensor       |       | float64 |
new_persons_fully_vaccinated                            | Tensor       |       | float64 |
new_persons_fully_vaccinated_janssen                    | Tensor       |       | float64 |
new_persons_fully_vaccinated_moderna                    | Tensor       |       | float64 |
new_persons_fully_vaccinated_pfizer                     | Tensor       |       | float64 |
new_persons_vaccinated                                  | Tensor       |       | float64 |
new_recovered                                           | Tensor       |       | float64 |
new_recovered_age_0                                     | Tensor       |       | float64 |
new_recovered_age_1                                     | Tensor       |       | float64 |
new_recovered_age_2                                     | Tensor       |       | float64 |
new_recovered_age_3                                     | Tensor       |       | float64 |
new_recovered_age_4                                     | Tensor       |       | float64 |
new_recovered_age_5                                     | Tensor       |       | float64 |
new_recovered_age_6                                     | Tensor       |       | float64 |
new_recovered_age_7                                     | Tensor       |       | float64 |
new_recovered_age_8                                     | Tensor       |       | float64 |
new_recovered_age_9                                     | Tensor       |       | float64 |
new_recovered_female                                    | Tensor       |       | float64 |
new_recovered_male                                      | Tensor       |       | float64 |
new_tested                                              | Tensor       |       | float64 |
new_tested_age_0                                        | Tensor       |       | float64 |
new_tested_age_1                                        | Tensor       |       | float64 |
new_tested_age_2                                        | Tensor       |       | float64 |
new_tested_age_3                                        | Tensor       |       | float64 |
new_tested_age_4                                        | Tensor       |       | float64 |
new_tested_age_5                                        | Tensor       |       | float64 |
new_tested_age_6                                        | Tensor       |       | float64 |
new_tested_age_7                                        | Tensor       |       | float64 |
new_tested_age_8                                        | Tensor       |       | float64 |
new_tested_age_9                                        | Tensor       |       | float64 |
new_tested_female                                       | Tensor       |       | float64 |
new_tested_male                                         | Tensor       |       | float64 |
new_vaccine_doses_administered                          | Tensor       |       | float64 |
new_vaccine_doses_administered_janssen                  | Tensor       |       | float64 |
new_vaccine_doses_administered_moderna                  | Tensor       |       | float64 |
new_vaccine_doses_administered_pfizer                   | Tensor       |       | float64 |
new_ventilator_patients                                 | Tensor       |       | float64 |
nurses_per_1000                                         | Tensor       |       | float64 |
openstreetmap_id                                        | Tensor       |       | string  |
out_of_pocket_health_expenditure_usd                    | Tensor       |       | float64 |
physicians_per_1000                                     | Tensor       |       | float64 |
place_id                                                | Tensor       |       | string  |
pollution_mortality_rate                                | Tensor       |       | float64 |
population                                              | Tensor       |       | float64 |
population_age_00_09                                    | Tensor       |       | float64 |
population_age_10_19                                    | Tensor       |       | float64 |
population_age_20_29                                    | Tensor       |       | float64 |
population_age_30_39                                    | Tensor       |       | float64 |
population_age_40_49                                    | Tensor       |       | float64 |
population_age_50_59                                    | Tensor       |       | float64 |
population_age_60_69                                    | Tensor       |       | float64 |
population_age_70_79                                    | Tensor       |       | float64 |
population_age_80_and_older                             | Tensor       |       | float64 |
population_clustered                                    | Tensor       |       | float64 |
population_density                                      | Tensor       |       | float64 |
population_female                                       | Tensor       |       | float64 |
population_largest_city                                 | Tensor       |       | float64 |
population_male                                         | Tensor       |       | float64 |
population_rural                                        | Tensor       |       | float64 |
population_urban                                        | Tensor       |       | float64 |
public_information_campaigns                            | Tensor       |       | float64 |
public_transport_closing                                | Tensor       |       | float64 |
rainfall_mm                                             | Tensor       |       | float64 |
relative_humidity                                       | Tensor       |       | float64 |
restrictions_on_gatherings                              | Tensor       |       | float64 |
restrictions_on_internal_movement                       | Tensor       |       | float64 |
school_closing                                          | Tensor       |       | float64 |
search_trends_abdominal_obesity                         | Tensor       |       | float64 |
search_trends_abdominal_pain                            | Tensor       |       | float64 |
search_trends_acne                                      | Tensor       |       | float64 |
search_trends_actinic_keratosis                         | Tensor       |       | float64 |
search_trends_acute_bronchitis                          | Tensor       |       | float64 |
search_trends_adrenal_crisis                            | Tensor       |       | float64 |
search_trends_ageusia                                   | Tensor       |       | float64 |
search_trends_alcoholism                                | Tensor       |       | float64 |
search_trends_allergic_conjunctivitis                   | Tensor       |       | float64 |
search_trends_allergy                                   | Tensor       |       | float64 |
search_trends_amblyopia                                 | Tensor       |       | float64 |
search_trends_amenorrhea                                | Tensor       |       | float64 |
search_trends_amnesia                                   | Tensor       |       | float64 |
search_trends_anal_fissure                              | Tensor       |       | float64 |
search_trends_anaphylaxis                               | Tensor       |       | float64 |
search_trends_anemia                                    | Tensor       |       | float64 |
search_trends_angina_pectoris                           | Tensor       |       | float64 |
search_trends_angioedema                                | Tensor       |       | float64 |
search_trends_angular_cheilitis                         | Tensor       |       | float64 |
search_trends_anosmia                                   | Tensor       |       | float64 |
search_trends_anxiety                                   | Tensor       |       | float64 |
search_trends_aphasia                                   | Tensor       |       | float64 |
search_trends_aphonia                                   | Tensor       |       | float64 |
search_trends_apnea                                     | Tensor       |       | float64 |
search_trends_arthralgia                                | Tensor       |       | float64 |
search_trends_arthritis                                 | Tensor       |       | float64 |
search_trends_ascites                                   | Tensor       |       | float64 |
search_trends_asperger_syndrome                         | Tensor       |       | float64 |
search_trends_asphyxia                                  | Tensor       |       | float64 |
search_trends_asthma                                    | Tensor       |       | float64 |
search_trends_astigmatism                               | Tensor       |       | float64 |
search_trends_ataxia                                    | Tensor       |       | float64 |
search_trends_atheroma                                  | Tensor       |       | float64 |
search_trends_attention_deficit_hyperactivity_disorder  | Tensor       |       | float64 |
search_trends_auditory_hallucination                    | Tensor       |       | float64 |
search_trends_autoimmune_disease                        | Tensor       |       | float64 |
search_trends_avoidant_personality_disorder             | Tensor       |       | float64 |
search_trends_back_pain                                 | Tensor       |       | float64 |
search_trends_bacterial_vaginosis                       | Tensor       |       | float64 |
search_trends_balance_disorder                          | Tensor       |       | float64 |
search_trends_beaus_lines                               | Tensor       |       | float64 |
search_trends_bells_palsy                               | Tensor       |       | float64 |
search_trends_biliary_colic                             | Tensor       |       | float64 |
search_trends_binge_eating                              | Tensor       |       | float64 |
search_trends_bleeding                                  | Tensor       |       | float64 |
search_trends_bleeding_on_probing                       | Tensor       |       | float64 |
search_trends_blepharospasm                             | Tensor       |       | float64 |
search_trends_bloating                                  | Tensor       |       | float64 |
search_trends_blood_in_stool                            | Tensor       |       | float64 |
search_trends_blurred_vision                            | Tensor       |       | float64 |
search_trends_blushing                                  | Tensor       |       | float64 |
search_trends_boil                                      | Tensor       |       | float64 |
search_trends_bone_fracture                             | Tensor       |       | float64 |
search_trends_bone_tumor                                | Tensor       |       | float64 |
search_trends_bowel_obstruction                         | Tensor       |       | float64 |
search_trends_bradycardia                               | Tensor       |       | float64 |
search_trends_braxton_hicks_contractions                | Tensor       |       | float64 |
search_trends_breakthrough_bleeding                     | Tensor       |       | float64 |
search_trends_breast_pain                               | Tensor       |       | float64 |
search_trends_bronchitis                                | Tensor       |       | float64 |
search_trends_bruise                                    | Tensor       |       | float64 |
search_trends_bruxism                                   | Tensor       |       | float64 |
search_trends_bunion                                    | Tensor       |       | float64 |
search_trends_burn                                      | Tensor       |       | float64 |
search_trends_burning_chest_pain                        | Tensor       |       | float64 |
search_trends_burning_mouth_syndrome                    | Tensor       |       | float64 |
search_trends_candidiasis                               | Tensor       |       | float64 |
search_trends_canker_sore                               | Tensor       |       | float64 |
search_trends_cardiac_arrest                            | Tensor       |       | float64 |
search_trends_carpal_tunnel_syndrome                    | Tensor       |       | float64 |
search_trends_cataplexy                                 | Tensor       |       | float64 |
search_trends_cataract                                  | Tensor       |       | float64 |
search_trends_chancre                                   | Tensor       |       | float64 |
search_trends_cheilitis                                 | Tensor       |       | float64 |
search_trends_chest_pain                                | Tensor       |       | float64 |
search_trends_chills                                    | Tensor       |       | float64 |
search_trends_chorea                                    | Tensor       |       | float64 |
search_trends_chronic_pain                              | Tensor       |       | float64 |
search_trends_cirrhosis                                 | Tensor       |       | float64 |
search_trends_cleft_lip_and_cleft_palate                | Tensor       |       | float64 |
search_trends_clouding_of_consciousness                 | Tensor       |       | float64 |
search_trends_cluster_headache                          | Tensor       |       | float64 |
search_trends_colitis                                   | Tensor       |       | float64 |
search_trends_coma                                      | Tensor       |       | float64 |
search_trends_common_cold                               | Tensor       |       | float64 |
search_trends_compulsive_behavior                       | Tensor       |       | float64 |
search_trends_compulsive_hoarding                       | Tensor       |       | float64 |
search_trends_confusion                                 | Tensor       |       | float64 |
search_trends_congenital_heart_defect                   | Tensor       |       | float64 |
search_trends_conjunctivitis                            | Tensor       |       | float64 |
search_trends_constipation                              | Tensor       |       | float64 |
search_trends_convulsion                                | Tensor       |       | float64 |
search_trends_cough                                     | Tensor       |       | float64 |
search_trends_crackles                                  | Tensor       |       | float64 |
search_trends_cramp                                     | Tensor       |       | float64 |
search_trends_crepitus                                  | Tensor       |       | float64 |
search_trends_croup                                     | Tensor       |       | float64 |
search_trends_cyanosis                                  | Tensor       |       | float64 |
search_trends_dandruff                                  | Tensor       |       | float64 |
search_trends_delayed_onset_muscle_soreness             | Tensor       |       | float64 |
search_trends_dementia                                  | Tensor       |       | float64 |
search_trends_dentin_hypersensitivity                   | Tensor       |       | float64 |
search_trends_depersonalization                         | Tensor       |       | float64 |
search_trends_depression                                | Tensor       |       | float64 |
search_trends_dermatitis                                | Tensor       |       | float64 |
search_trends_desquamation                              | Tensor       |       | float64 |
search_trends_developmental_disability                  | Tensor       |       | float64 |
search_trends_diabetes                                  | Tensor       |       | float64 |
search_trends_diabetic_ketoacidosis                     | Tensor       |       | float64 |
search_trends_diarrhea                                  | Tensor       |       | float64 |
search_trends_dizziness                                 | Tensor       |       | float64 |
search_trends_dry_eye_syndrome                          | Tensor       |       | float64 |
search_trends_dysautonomia                              | Tensor       |       | float64 |
search_trends_dysgeusia                                 | Tensor       |       | float64 |
search_trends_dysmenorrhea                              | Tensor       |       | float64 |
search_trends_dyspareunia                               | Tensor       |       | float64 |
search_trends_dysphagia                                 | Tensor       |       | float64 |
search_trends_dysphoria                                 | Tensor       |       | float64 |
search_trends_dystonia                                  | Tensor       |       | float64 |
search_trends_dysuria                                   | Tensor       |       | float64 |
search_trends_ear_pain                                  | Tensor       |       | float64 |
search_trends_eczema                                    | Tensor       |       | float64 |
search_trends_edema                                     | Tensor       |       | float64 |
search_trends_encephalitis                              | Tensor       |       | float64 |
search_trends_encephalopathy                            | Tensor       |       | float64 |
search_trends_epidermoid_cyst                           | Tensor       |       | float64 |
search_trends_epilepsy                                  | Tensor       |       | float64 |
search_trends_epiphora                                  | Tensor       |       | float64 |
search_trends_erectile_dysfunction                      | Tensor       |       | float64 |
search_trends_erythema                                  | Tensor       |       | float64 |
search_trends_erythema_chronicum_migrans                | Tensor       |       | float64 |
search_trends_esophagitis                               | Tensor       |       | float64 |
search_trends_excessive_daytime_sleepiness              | Tensor       |       | float64 |
search_trends_eye_pain                                  | Tensor       |       | float64 |
search_trends_eye_strain                                | Tensor       |       | float64 |
search_trends_facial_nerve_paralysis                    | Tensor       |       | float64 |
search_trends_facial_swelling                           | Tensor       |       | float64 |
search_trends_fasciculation                             | Tensor       |       | float64 |
search_trends_fatigue                                   | Tensor       |       | float64 |
search_trends_fatty_liver_disease                       | Tensor       |       | float64 |
search_trends_fecal_incontinence                        | Tensor       |       | float64 |
search_trends_fever                                     | Tensor       |       | float64 |
search_trends_fibrillation                              | Tensor       |       | float64 |
search_trends_fibrocystic_breast_changes                | Tensor       |       | float64 |
search_trends_fibromyalgia                              | Tensor       |       | float64 |
search_trends_flatulence                                | Tensor       |       | float64 |
search_trends_floater                                   | Tensor       |       | float64 |
search_trends_focal_seizure                             | Tensor       |       | float64 |
search_trends_folate_deficiency                         | Tensor       |       | float64 |
search_trends_food_craving                              | Tensor       |       | float64 |
search_trends_food_intolerance                          | Tensor       |       | float64 |
search_trends_frequent_urination                        | Tensor       |       | float64 |
search_trends_gastroesophageal_reflux_disease           | Tensor       |       | float64 |
search_trends_gastroparesis                             | Tensor       |       | float64 |
search_trends_generalized_anxiety_disorder              | Tensor       |       | float64 |
search_trends_genital_wart                              | Tensor       |       | float64 |
search_trends_gingival_recession                        | Tensor       |       | float64 |
search_trends_gingivitis                                | Tensor       |       | float64 |
search_trends_globus_pharyngis                          | Tensor       |       | float64 |
search_trends_goitre                                    | Tensor       |       | float64 |
search_trends_gout                                      | Tensor       |       | float64 |
search_trends_grandiosity                               | Tensor       |       | float64 |
search_trends_granuloma                                 | Tensor       |       | float64 |
search_trends_guilt                                     | Tensor       |       | float64 |
search_trends_hair_loss                                 | Tensor       |       | float64 |
search_trends_halitosis                                 | Tensor       |       | float64 |
search_trends_hay_fever                                 | Tensor       |       | float64 |
search_trends_headache                                  | Tensor       |       | float64 |
search_trends_heart_arrhythmia                          | Tensor       |       | float64 |
search_trends_heart_murmur                              | Tensor       |       | float64 |
search_trends_heartburn                                 | Tensor       |       | float64 |
search_trends_hematochezia                              | Tensor       |       | float64 |
search_trends_hematoma                                  | Tensor       |       | float64 |
search_trends_hematuria                                 | Tensor       |       | float64 |
search_trends_hemolysis                                 | Tensor       |       | float64 |
search_trends_hemoptysis                                | Tensor       |       | float64 |
search_trends_hemorrhoids                               | Tensor       |       | float64 |
search_trends_hepatic_encephalopathy                    | Tensor       |       | float64 |
search_trends_hepatitis                                 | Tensor       |       | float64 |
search_trends_hepatotoxicity                            | Tensor       |       | float64 |
search_trends_hiccup                                    | Tensor       |       | float64 |
search_trends_hip_pain                                  | Tensor       |       | float64 |
search_trends_hives                                     | Tensor       |       | float64 |
search_trends_hot_flash                                 | Tensor       |       | float64 |
search_trends_hydrocephalus                             | Tensor       |       | float64 |
search_trends_hypercalcaemia                            | Tensor       |       | float64 |
search_trends_hypercapnia                               | Tensor       |       | float64 |
search_trends_hypercholesterolemia                      | Tensor       |       | float64 |
search_trends_hyperemesis_gravidarum                    | Tensor       |       | float64 |
search_trends_hyperglycemia                             | Tensor       |       | float64 |
search_trends_hyperhidrosis                             | Tensor       |       | float64 |
search_trends_hyperkalemia                              | Tensor       |       | float64 |
search_trends_hyperlipidemia                            | Tensor       |       | float64 |
search_trends_hypermobility                             | Tensor       |       | float64 |
search_trends_hyperpigmentation                         | Tensor       |       | float64 |
search_trends_hypersomnia                               | Tensor       |       | float64 |
search_trends_hypertension                              | Tensor       |       | float64 |
search_trends_hyperthermia                              | Tensor       |       | float64 |
search_trends_hyperthyroidism                           | Tensor       |       | float64 |
search_trends_hypertriglyceridemia                      | Tensor       |       | float64 |
search_trends_hypertrophy                               | Tensor       |       | float64 |
search_trends_hyperventilation                          | Tensor       |       | float64 |
search_trends_hypocalcaemia                             | Tensor       |       | float64 |
search_trends_hypochondriasis                           | Tensor       |       | float64 |
search_trends_hypoglycemia                              | Tensor       |       | float64 |
search_trends_hypogonadism                              | Tensor       |       | float64 |
search_trends_hypokalemia                               | Tensor       |       | float64 |
search_trends_hypomania                                 | Tensor       |       | float64 |
search_trends_hyponatremia                              | Tensor       |       | float64 |
search_trends_hypotension                               | Tensor       |       | float64 |
search_trends_hypothyroidism                            | Tensor       |       | float64 |
search_trends_hypoxemia                                 | Tensor       |       | float64 |
search_trends_hypoxia                                   | Tensor       |       | float64 |
search_trends_impetigo                                  | Tensor       |       | float64 |
search_trends_implantation_bleeding                     | Tensor       |       | float64 |
search_trends_impulsivity                               | Tensor       |       | float64 |
search_trends_indigestion                               | Tensor       |       | float64 |
search_trends_infection                                 | Tensor       |       | float64 |
search_trends_inflammation                              | Tensor       |       | float64 |
search_trends_inflammatory_bowel_disease                | Tensor       |       | float64 |
search_trends_ingrown_hair                              | Tensor       |       | float64 |
search_trends_insomnia                                  | Tensor       |       | float64 |
search_trends_insulin_resistance                        | Tensor       |       | float64 |
search_trends_intermenstrual_bleeding                   | Tensor       |       | float64 |
search_trends_intracranial_pressure                     | Tensor       |       | float64 |
search_trends_iron_deficiency                           | Tensor       |       | float64 |
search_trends_irregular_menstruation                    | Tensor       |       | float64 |
search_trends_itch                                      | Tensor       |       | float64 |
search_trends_jaundice                                  | Tensor       |       | float64 |
search_trends_kidney_failure                            | Tensor       |       | float64 |
search_trends_kidney_stone                              | Tensor       |       | float64 |
search_trends_knee_pain                                 | Tensor       |       | float64 |
search_trends_kyphosis                                  | Tensor       |       | float64 |
search_trends_lactose_intolerance                       | Tensor       |       | float64 |
search_trends_laryngitis                                | Tensor       |       | float64 |
search_trends_leg_cramps                                | Tensor       |       | float64 |
search_trends_lesion                                    | Tensor       |       | float64 |
search_trends_leukorrhea                                | Tensor       |       | float64 |
search_trends_lightheadedness                           | Tensor       |       | float64 |
search_trends_low_back_pain                             | Tensor       |       | float64 |
search_trends_low_grade_fever                           | Tensor       |       | float64 |
search_trends_lymphedema                                | Tensor       |       | float64 |
search_trends_major_depressive_disorder                 | Tensor       |       | float64 |
search_trends_malabsorption                             | Tensor       |       | float64 |
search_trends_male_infertility                          | Tensor       |       | float64 |
search_trends_manic_disorder                            | Tensor       |       | float64 |
search_trends_melasma                                   | Tensor       |       | float64 |
search_trends_melena                                    | Tensor       |       | float64 |
search_trends_meningitis                                | Tensor       |       | float64 |
search_trends_menorrhagia                               | Tensor       |       | float64 |
search_trends_middle_back_pain                          | Tensor       |       | float64 |
search_trends_migraine                                  | Tensor       |       | float64 |
search_trends_milium                                    | Tensor       |       | float64 |
search_trends_mitral_insufficiency                      | Tensor       |       | float64 |
search_trends_mood_disorder                             | Tensor       |       | float64 |
search_trends_mood_swing                                | Tensor       |       | float64 |
search_trends_morning_sickness                          | Tensor       |       | float64 |
search_trends_motion_sickness                           | Tensor       |       | float64 |
search_trends_mouth_ulcer                               | Tensor       |       | float64 |
search_trends_muscle_atrophy                            | Tensor       |       | float64 |
search_trends_muscle_weakness                           | Tensor       |       | float64 |
search_trends_myalgia                                   | Tensor       |       | float64 |
search_trends_mydriasis                                 | Tensor       |       | float64 |
search_trends_myocardial_infarction                     | Tensor       |       | float64 |
search_trends_myoclonus                                 | Tensor       |       | float64 |
search_trends_nasal_congestion                          | Tensor       |       | float64 |
search_trends_nasal_polyp                               | Tensor       |       | float64 |
search_trends_nausea                                    | Tensor       |       | float64 |
search_trends_neck_mass                                 | Tensor       |       | float64 |
search_trends_neck_pain                                 | Tensor       |       | float64 |
search_trends_neonatal_jaundice                         | Tensor       |       | float64 |
search_trends_nerve_injury                              | Tensor       |       | float64 |
search_trends_neuralgia                                 | Tensor       |       | float64 |
search_trends_neutropenia                               | Tensor       |       | float64 |
search_trends_night_sweats                              | Tensor       |       | float64 |
search_trends_night_terror                              | Tensor       |       | float64 |
search_trends_nocturnal_enuresis                        | Tensor       |       | float64 |
search_trends_nodule                                    | Tensor       |       | float64 |
search_trends_nosebleed                                 | Tensor       |       | float64 |
search_trends_nystagmus                                 | Tensor       |       | float64 |
search_trends_obesity                                   | Tensor       |       | float64 |
search_trends_onychorrhexis                             | Tensor       |       | float64 |
search_trends_oral_candidiasis                          | Tensor       |       | float64 |
search_trends_orthostatic_hypotension                   | Tensor       |       | float64 |
search_trends_osteopenia                                | Tensor       |       | float64 |
search_trends_osteophyte                                | Tensor       |       | float64 |
search_trends_osteoporosis                              | Tensor       |       | float64 |
search_trends_otitis                                    | Tensor       |       | float64 |
search_trends_otitis_externa                            | Tensor       |       | float64 |
search_trends_otitis_media                              | Tensor       |       | float64 |
search_trends_pain                                      | Tensor       |       | float64 |
search_trends_palpitations                              | Tensor       |       | float64 |
search_trends_pancreatitis                              | Tensor       |       | float64 |
search_trends_panic_attack                              | Tensor       |       | float64 |
search_trends_papule                                    | Tensor       |       | float64 |
search_trends_paranoia                                  | Tensor       |       | float64 |
search_trends_paresthesia                               | Tensor       |       | float64 |
search_trends_pelvic_inflammatory_disease               | Tensor       |       | float64 |
search_trends_pericarditis                              | Tensor       |       | float64 |
search_trends_periodontal_disease                       | Tensor       |       | float64 |
search_trends_periorbital_puffiness                     | Tensor       |       | float64 |
search_trends_peripheral_neuropathy                     | Tensor       |       | float64 |
search_trends_perspiration                              | Tensor       |       | float64 |
search_trends_petechia                                  | Tensor       |       | float64 |
search_trends_phlegm                                    | Tensor       |       | float64 |
search_trends_photodermatitis                           | Tensor       |       | float64 |
search_trends_photophobia                               | Tensor       |       | float64 |
search_trends_photopsia                                 | Tensor       |       | float64 |
search_trends_pleural_effusion                          | Tensor       |       | float64 |
search_trends_pleurisy                                  | Tensor       |       | float64 |
search_trends_pneumonia                                 | Tensor       |       | float64 |
search_trends_podalgia                                  | Tensor       |       | float64 |
search_trends_polycythemia                              | Tensor       |       | float64 |
search_trends_polydipsia                                | Tensor       |       | float64 |
search_trends_polyneuropathy                            | Tensor       |       | float64 |
search_trends_polyuria                                  | Tensor       |       | float64 |
search_trends_poor_posture                              | Tensor       |       | float64 |
search_trends_post_nasal_drip                           | Tensor       |       | float64 |
search_trends_postural_orthostatic_tachycardia_syndrome | Tensor       |       | float64 |
search_trends_prediabetes                               | Tensor       |       | float64 |
search_trends_proteinuria                               | Tensor       |       | float64 |
search_trends_pruritus_ani                              | Tensor       |       | float64 |
search_trends_psychosis                                 | Tensor       |       | float64 |
search_trends_ptosis                                    | Tensor       |       | float64 |
search_trends_pulmonary_edema                           | Tensor       |       | float64 |
search_trends_pulmonary_hypertension                    | Tensor       |       | float64 |
search_trends_purpura                                   | Tensor       |       | float64 |
search_trends_pus                                       | Tensor       |       | float64 |
search_trends_pyelonephritis                            | Tensor       |       | float64 |
search_trends_radiculopathy                             | Tensor       |       | float64 |
search_trends_rectal_pain                               | Tensor       |       | float64 |
search_trends_rectal_prolapse                           | Tensor       |       | float64 |
search_trends_red_eye                                   | Tensor       |       | float64 |
search_trends_renal_colic                               | Tensor       |       | float64 |
search_trends_restless_legs_syndrome                    | Tensor       |       | float64 |
search_trends_rheum                                     | Tensor       |       | float64 |
search_trends_rhinitis                                  | Tensor       |       | float64 |
search_trends_rhinorrhea                                | Tensor       |       | float64 |
search_trends_rosacea                                   | Tensor       |       | float64 |
search_trends_round_ligament_pain                       | Tensor       |       | float64 |
search_trends_rumination                                | Tensor       |       | float64 |
search_trends_scar                                      | Tensor       |       | float64 |
search_trends_sciatica                                  | Tensor       |       | float64 |
search_trends_scoliosis                                 | Tensor       |       | float64 |
search_trends_seborrheic_dermatitis                     | Tensor       |       | float64 |
search_trends_self_harm                                 | Tensor       |       | float64 |
search_trends_sensitivity_to_sound                      | Tensor       |       | float64 |
search_trends_sexual_dysfunction                        | Tensor       |       | float64 |
search_trends_shallow_breathing                         | Tensor       |       | float64 |
search_trends_sharp_pain                                | Tensor       |       | float64 |
search_trends_shivering                                 | Tensor       |       | float64 |
search_trends_shortness_of_breath                       | Tensor       |       | float64 |
search_trends_shyness                                   | Tensor       |       | float64 |
search_trends_sinusitis                                 | Tensor       |       | float64 |
search_trends_skin_condition                            | Tensor       |       | float64 |
search_trends_skin_rash                                 | Tensor       |       | float64 |
search_trends_skin_tag                                  | Tensor       |       | float64 |
search_trends_skin_ulcer                                | Tensor       |       | float64 |
search_trends_sleep_apnea                               | Tensor       |       | float64 |
search_trends_sleep_deprivation                         | Tensor       |       | float64 |
search_trends_sleep_disorder                            | Tensor       |       | float64 |
search_trends_snoring                                   | Tensor       |       | float64 |
search_trends_sore_throat                               | Tensor       |       | float64 |
search_trends_spasticity                                | Tensor       |       | float64 |
search_trends_splenomegaly                              | Tensor       |       | float64 |
search_trends_sputum                                    | Tensor       |       | float64 |
search_trends_stomach_rumble                            | Tensor       |       | float64 |
search_trends_strabismus                                | Tensor       |       | float64 |
search_trends_stretch_marks                             | Tensor       |       | float64 |
search_trends_stridor                                   | Tensor       |       | float64 |
search_trends_stroke                                    | Tensor       |       | float64 |
search_trends_stuttering                                | Tensor       |       | float64 |
search_trends_subdural_hematoma                         | Tensor       |       | float64 |
search_trends_suicidal_ideation                         | Tensor       |       | float64 |
search_trends_swelling                                  | Tensor       |       | float64 |
search_trends_swollen_feet                              | Tensor       |       | float64 |
search_trends_swollen_lymph_nodes                       | Tensor       |       | float64 |
search_trends_syncope                                   | Tensor       |       | float64 |
search_trends_tachycardia                               | Tensor       |       | float64 |
search_trends_tachypnea                                 | Tensor       |       | float64 |
search_trends_telangiectasia                            | Tensor       |       | float64 |
search_trends_tenderness                                | Tensor       |       | float64 |
search_trends_testicular_pain                           | Tensor       |       | float64 |
search_trends_throat_irritation                         | Tensor       |       | float64 |
search_trends_thrombocytopenia                          | Tensor       |       | float64 |
search_trends_thyroid_nodule                            | Tensor       |       | float64 |
search_trends_tic                                       | Tensor       |       | float64 |
search_trends_tinnitus                                  | Tensor       |       | float64 |
search_trends_tonsillitis                               | Tensor       |       | float64 |
search_trends_toothache                                 | Tensor       |       | float64 |
search_trends_tremor                                    | Tensor       |       | float64 |
search_trends_trichoptilosis                            | Tensor       |       | float64 |
search_trends_tumor                                     | Tensor       |       | float64 |
search_trends_type_2_diabetes                           | Tensor       |       | float64 |
search_trends_unconsciousness                           | Tensor       |       | float64 |
search_trends_underweight                               | Tensor       |       | float64 |
search_trends_upper_respiratory_tract_infection         | Tensor       |       | float64 |
search_trends_urethritis                                | Tensor       |       | float64 |
search_trends_urinary_incontinence                      | Tensor       |       | float64 |
search_trends_urinary_tract_infection                   | Tensor       |       | float64 |
search_trends_urinary_urgency                           | Tensor       |       | float64 |
search_trends_uterine_contraction                       | Tensor       |       | float64 |
search_trends_vaginal_bleeding                          | Tensor       |       | float64 |
search_trends_vaginal_discharge                         | Tensor       |       | float64 |
search_trends_vaginitis                                 | Tensor       |       | float64 |
search_trends_varicose_veins                            | Tensor       |       | float64 |
search_trends_vasculitis                                | Tensor       |       | float64 |
search_trends_ventricular_fibrillation                  | Tensor       |       | float64 |
search_trends_ventricular_tachycardia                   | Tensor       |       | float64 |
search_trends_vertigo                                   | Tensor       |       | float64 |
search_trends_viral_pneumonia                           | Tensor       |       | float64 |
search_trends_visual_acuity                             | Tensor       |       | float64 |
search_trends_vomiting                                  | Tensor       |       | float64 |
search_trends_wart                                      | Tensor       |       | float64 |
search_trends_water_retention                           | Tensor       |       | float64 |
search_trends_weakness                                  | Tensor       |       | float64 |
search_trends_weight_gain                               | Tensor       |       | float64 |
search_trends_wheeze                                    | Tensor       |       | float64 |
search_trends_xeroderma                                 | Tensor       |       | float64 |
search_trends_xerostomia                                | Tensor       |       | float64 |
search_trends_yawn                                      | Tensor       |       | float64 |
smoking_prevalence                                      | Tensor       |       | float64 |
snowfall_mm                                             | Tensor       |       | float64 |
stay_at_home_requirements                               | Tensor       |       | float64 |
stringency_index                                        | Tensor       |       | float64 |
subregion1_code                                         | Tensor       |       | string  |
subregion1_name                                         | Tensor       |       | string  |
subregion2_code                                         | Tensor       |       | string  |
subregion2_name                                         | Tensor       |       | string  |
testing_policy                                          | Tensor       |       | float64 |
vaccination_policy                                      | Tensor       |       | float64 |
wikidata_id                                             | Tensor       |       | string  |
workplace_closing                                       | Tensor       |       | float64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/covid19-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@article{Wahltinez2020,
  author = "O. Wahltinez and others",
  year = 2020,
  title = "COVID-19 Open-Data: curating a fine-grained, global-scale data repository for SARS-CoV-2",
  note = "Work in progress",
  url = {https://goo.gle/covid-19-open-data},
}
```

