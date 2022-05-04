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
    'adult_female_mortality_rate': tf.float64,
    'adult_male_mortality_rate': tf.float64,
    'age_bin_0': tf.string,
    'age_bin_1': tf.string,
    'age_bin_2': tf.string,
    'age_bin_3': tf.string,
    'age_bin_4': tf.string,
    'age_bin_5': tf.string,
    'age_bin_6': tf.string,
    'age_bin_7': tf.string,
    'age_bin_8': tf.string,
    'age_bin_9': tf.string,
    'aggregation_level': tf.float64,
    'area_rural_sq_km': tf.float64,
    'area_sq_km': tf.float64,
    'area_urban_sq_km': tf.float64,
    'average_temperature_celsius': tf.float64,
    'cancel_public_events': tf.float64,
    'comorbidity_mortality_rate': tf.float64,
    'contact_tracing': tf.float64,
    'country_code': tf.string,
    'country_name': tf.string,
    'cumulative_confirmed': tf.float64,
    'cumulative_confirmed_age_0': tf.float64,
    'cumulative_confirmed_age_1': tf.float64,
    'cumulative_confirmed_age_2': tf.float64,
    'cumulative_confirmed_age_3': tf.float64,
    'cumulative_confirmed_age_4': tf.float64,
    'cumulative_confirmed_age_5': tf.float64,
    'cumulative_confirmed_age_6': tf.float64,
    'cumulative_confirmed_age_7': tf.float64,
    'cumulative_confirmed_age_8': tf.float64,
    'cumulative_confirmed_age_9': tf.float64,
    'cumulative_confirmed_female': tf.float64,
    'cumulative_confirmed_male': tf.float64,
    'cumulative_deceased': tf.float64,
    'cumulative_deceased_age_0': tf.float64,
    'cumulative_deceased_age_1': tf.float64,
    'cumulative_deceased_age_2': tf.float64,
    'cumulative_deceased_age_3': tf.float64,
    'cumulative_deceased_age_4': tf.float64,
    'cumulative_deceased_age_5': tf.float64,
    'cumulative_deceased_age_6': tf.float64,
    'cumulative_deceased_age_7': tf.float64,
    'cumulative_deceased_age_8': tf.float64,
    'cumulative_deceased_age_9': tf.float64,
    'cumulative_deceased_female': tf.float64,
    'cumulative_deceased_male': tf.float64,
    'cumulative_hospitalized_patients': tf.float64,
    'cumulative_hospitalized_patients_age_0': tf.float64,
    'cumulative_hospitalized_patients_age_1': tf.float64,
    'cumulative_hospitalized_patients_age_2': tf.float64,
    'cumulative_hospitalized_patients_age_3': tf.float64,
    'cumulative_hospitalized_patients_age_4': tf.float64,
    'cumulative_hospitalized_patients_age_5': tf.float64,
    'cumulative_hospitalized_patients_age_6': tf.float64,
    'cumulative_hospitalized_patients_age_7': tf.float64,
    'cumulative_hospitalized_patients_age_8': tf.float64,
    'cumulative_hospitalized_patients_age_9': tf.float64,
    'cumulative_hospitalized_patients_female': tf.float64,
    'cumulative_hospitalized_patients_male': tf.float64,
    'cumulative_intensive_care_patients': tf.float64,
    'cumulative_intensive_care_patients_age_0': tf.float64,
    'cumulative_intensive_care_patients_age_1': tf.float64,
    'cumulative_intensive_care_patients_age_2': tf.float64,
    'cumulative_intensive_care_patients_age_3': tf.float64,
    'cumulative_intensive_care_patients_age_4': tf.float64,
    'cumulative_intensive_care_patients_age_5': tf.float64,
    'cumulative_intensive_care_patients_age_6': tf.float64,
    'cumulative_intensive_care_patients_age_7': tf.float64,
    'cumulative_intensive_care_patients_age_8': tf.float64,
    'cumulative_intensive_care_patients_age_9': tf.float64,
    'cumulative_intensive_care_patients_female': tf.float64,
    'cumulative_intensive_care_patients_male': tf.float64,
    'cumulative_persons_fully_vaccinated': tf.float64,
    'cumulative_persons_fully_vaccinated_janssen': tf.float64,
    'cumulative_persons_fully_vaccinated_moderna': tf.float64,
    'cumulative_persons_fully_vaccinated_pfizer': tf.float64,
    'cumulative_persons_vaccinated': tf.float64,
    'cumulative_recovered': tf.float64,
    'cumulative_recovered_age_0': tf.float64,
    'cumulative_recovered_age_1': tf.float64,
    'cumulative_recovered_age_2': tf.float64,
    'cumulative_recovered_age_3': tf.float64,
    'cumulative_recovered_age_4': tf.float64,
    'cumulative_recovered_age_5': tf.float64,
    'cumulative_recovered_age_6': tf.float64,
    'cumulative_recovered_age_7': tf.float64,
    'cumulative_recovered_age_8': tf.float64,
    'cumulative_recovered_age_9': tf.float64,
    'cumulative_recovered_female': tf.float64,
    'cumulative_recovered_male': tf.float64,
    'cumulative_tested': tf.float64,
    'cumulative_tested_age_0': tf.float64,
    'cumulative_tested_age_1': tf.float64,
    'cumulative_tested_age_2': tf.float64,
    'cumulative_tested_age_3': tf.float64,
    'cumulative_tested_age_4': tf.float64,
    'cumulative_tested_age_5': tf.float64,
    'cumulative_tested_age_6': tf.float64,
    'cumulative_tested_age_7': tf.float64,
    'cumulative_tested_age_8': tf.float64,
    'cumulative_tested_age_9': tf.float64,
    'cumulative_tested_female': tf.float64,
    'cumulative_tested_male': tf.float64,
    'cumulative_vaccine_doses_administered': tf.float64,
    'cumulative_vaccine_doses_administered_janssen': tf.float64,
    'cumulative_vaccine_doses_administered_moderna': tf.float64,
    'cumulative_vaccine_doses_administered_pfizer': tf.float64,
    'cumulative_ventilator_patients': tf.float64,
    'current_hospitalized_patients': tf.float64,
    'current_intensive_care_patients': tf.float64,
    'current_ventilator_patients': tf.float64,
    'datacommons_id': tf.string,
    'date': tf.string,
    'debt_relief': tf.float64,
    'dew_point': tf.float64,
    'diabetes_prevalence': tf.float64,
    'elevation_m': tf.float64,
    'emergency_investment_in_healthcare': tf.float64,
    'facial_coverings': tf.float64,
    'fiscal_measures': tf.float64,
    'gdp_per_capita_usd': tf.float64,
    'gdp_usd': tf.float64,
    'health_expenditure_usd': tf.float64,
    'hospital_beds_per_1000': tf.float64,
    'human_capital_index': tf.float64,
    'human_development_index': tf.float64,
    'income_support': tf.float64,
    'infant_mortality_rate': tf.float64,
    'international_support': tf.float64,
    'international_travel_controls': tf.float64,
    'investment_in_vaccines': tf.float64,
    'iso_3166_1_alpha_2': tf.string,
    'iso_3166_1_alpha_3': tf.string,
    'latitude': tf.float64,
    'life_expectancy': tf.float64,
    'locality_code': tf.string,
    'locality_name': tf.string,
    'location_key': tf.string,
    'longitude': tf.float64,
    'maximum_temperature_celsius': tf.float64,
    'minimum_temperature_celsius': tf.float64,
    'mobility_grocery_and_pharmacy': tf.float64,
    'mobility_parks': tf.float64,
    'mobility_residential': tf.float64,
    'mobility_retail_and_recreation': tf.float64,
    'mobility_transit_stations': tf.float64,
    'mobility_workplaces': tf.float64,
    'new_confirmed': tf.float64,
    'new_confirmed_age_0': tf.float64,
    'new_confirmed_age_1': tf.float64,
    'new_confirmed_age_2': tf.float64,
    'new_confirmed_age_3': tf.float64,
    'new_confirmed_age_4': tf.float64,
    'new_confirmed_age_5': tf.float64,
    'new_confirmed_age_6': tf.float64,
    'new_confirmed_age_7': tf.float64,
    'new_confirmed_age_8': tf.float64,
    'new_confirmed_age_9': tf.float64,
    'new_confirmed_female': tf.float64,
    'new_confirmed_male': tf.float64,
    'new_deceased': tf.float64,
    'new_deceased_age_0': tf.float64,
    'new_deceased_age_1': tf.float64,
    'new_deceased_age_2': tf.float64,
    'new_deceased_age_3': tf.float64,
    'new_deceased_age_4': tf.float64,
    'new_deceased_age_5': tf.float64,
    'new_deceased_age_6': tf.float64,
    'new_deceased_age_7': tf.float64,
    'new_deceased_age_8': tf.float64,
    'new_deceased_age_9': tf.float64,
    'new_deceased_female': tf.float64,
    'new_deceased_male': tf.float64,
    'new_hospitalized_patients': tf.float64,
    'new_hospitalized_patients_age_0': tf.float64,
    'new_hospitalized_patients_age_1': tf.float64,
    'new_hospitalized_patients_age_2': tf.float64,
    'new_hospitalized_patients_age_3': tf.float64,
    'new_hospitalized_patients_age_4': tf.float64,
    'new_hospitalized_patients_age_5': tf.float64,
    'new_hospitalized_patients_age_6': tf.float64,
    'new_hospitalized_patients_age_7': tf.float64,
    'new_hospitalized_patients_age_8': tf.float64,
    'new_hospitalized_patients_age_9': tf.float64,
    'new_hospitalized_patients_female': tf.float64,
    'new_hospitalized_patients_male': tf.float64,
    'new_intensive_care_patients': tf.float64,
    'new_intensive_care_patients_age_0': tf.float64,
    'new_intensive_care_patients_age_1': tf.float64,
    'new_intensive_care_patients_age_2': tf.float64,
    'new_intensive_care_patients_age_3': tf.float64,
    'new_intensive_care_patients_age_4': tf.float64,
    'new_intensive_care_patients_age_5': tf.float64,
    'new_intensive_care_patients_age_6': tf.float64,
    'new_intensive_care_patients_age_7': tf.float64,
    'new_intensive_care_patients_age_8': tf.float64,
    'new_intensive_care_patients_age_9': tf.float64,
    'new_intensive_care_patients_female': tf.float64,
    'new_intensive_care_patients_male': tf.float64,
    'new_persons_fully_vaccinated': tf.float64,
    'new_persons_fully_vaccinated_janssen': tf.float64,
    'new_persons_fully_vaccinated_moderna': tf.float64,
    'new_persons_fully_vaccinated_pfizer': tf.float64,
    'new_persons_vaccinated': tf.float64,
    'new_recovered': tf.float64,
    'new_recovered_age_0': tf.float64,
    'new_recovered_age_1': tf.float64,
    'new_recovered_age_2': tf.float64,
    'new_recovered_age_3': tf.float64,
    'new_recovered_age_4': tf.float64,
    'new_recovered_age_5': tf.float64,
    'new_recovered_age_6': tf.float64,
    'new_recovered_age_7': tf.float64,
    'new_recovered_age_8': tf.float64,
    'new_recovered_age_9': tf.float64,
    'new_recovered_female': tf.float64,
    'new_recovered_male': tf.float64,
    'new_tested': tf.float64,
    'new_tested_age_0': tf.float64,
    'new_tested_age_1': tf.float64,
    'new_tested_age_2': tf.float64,
    'new_tested_age_3': tf.float64,
    'new_tested_age_4': tf.float64,
    'new_tested_age_5': tf.float64,
    'new_tested_age_6': tf.float64,
    'new_tested_age_7': tf.float64,
    'new_tested_age_8': tf.float64,
    'new_tested_age_9': tf.float64,
    'new_tested_female': tf.float64,
    'new_tested_male': tf.float64,
    'new_vaccine_doses_administered': tf.float64,
    'new_vaccine_doses_administered_janssen': tf.float64,
    'new_vaccine_doses_administered_moderna': tf.float64,
    'new_vaccine_doses_administered_pfizer': tf.float64,
    'new_ventilator_patients': tf.float64,
    'nurses_per_1000': tf.float64,
    'openstreetmap_id': tf.string,
    'out_of_pocket_health_expenditure_usd': tf.float64,
    'physicians_per_1000': tf.float64,
    'place_id': tf.string,
    'pollution_mortality_rate': tf.float64,
    'population': tf.float64,
    'population_age_00_09': tf.float64,
    'population_age_10_19': tf.float64,
    'population_age_20_29': tf.float64,
    'population_age_30_39': tf.float64,
    'population_age_40_49': tf.float64,
    'population_age_50_59': tf.float64,
    'population_age_60_69': tf.float64,
    'population_age_70_79': tf.float64,
    'population_age_80_and_older': tf.float64,
    'population_clustered': tf.float64,
    'population_density': tf.float64,
    'population_female': tf.float64,
    'population_largest_city': tf.float64,
    'population_male': tf.float64,
    'population_rural': tf.float64,
    'population_urban': tf.float64,
    'public_information_campaigns': tf.float64,
    'public_transport_closing': tf.float64,
    'rainfall_mm': tf.float64,
    'relative_humidity': tf.float64,
    'restrictions_on_gatherings': tf.float64,
    'restrictions_on_internal_movement': tf.float64,
    'school_closing': tf.float64,
    'search_trends_abdominal_obesity': tf.float64,
    'search_trends_abdominal_pain': tf.float64,
    'search_trends_acne': tf.float64,
    'search_trends_actinic_keratosis': tf.float64,
    'search_trends_acute_bronchitis': tf.float64,
    'search_trends_adrenal_crisis': tf.float64,
    'search_trends_ageusia': tf.float64,
    'search_trends_alcoholism': tf.float64,
    'search_trends_allergic_conjunctivitis': tf.float64,
    'search_trends_allergy': tf.float64,
    'search_trends_amblyopia': tf.float64,
    'search_trends_amenorrhea': tf.float64,
    'search_trends_amnesia': tf.float64,
    'search_trends_anal_fissure': tf.float64,
    'search_trends_anaphylaxis': tf.float64,
    'search_trends_anemia': tf.float64,
    'search_trends_angina_pectoris': tf.float64,
    'search_trends_angioedema': tf.float64,
    'search_trends_angular_cheilitis': tf.float64,
    'search_trends_anosmia': tf.float64,
    'search_trends_anxiety': tf.float64,
    'search_trends_aphasia': tf.float64,
    'search_trends_aphonia': tf.float64,
    'search_trends_apnea': tf.float64,
    'search_trends_arthralgia': tf.float64,
    'search_trends_arthritis': tf.float64,
    'search_trends_ascites': tf.float64,
    'search_trends_asperger_syndrome': tf.float64,
    'search_trends_asphyxia': tf.float64,
    'search_trends_asthma': tf.float64,
    'search_trends_astigmatism': tf.float64,
    'search_trends_ataxia': tf.float64,
    'search_trends_atheroma': tf.float64,
    'search_trends_attention_deficit_hyperactivity_disorder': tf.float64,
    'search_trends_auditory_hallucination': tf.float64,
    'search_trends_autoimmune_disease': tf.float64,
    'search_trends_avoidant_personality_disorder': tf.float64,
    'search_trends_back_pain': tf.float64,
    'search_trends_bacterial_vaginosis': tf.float64,
    'search_trends_balance_disorder': tf.float64,
    'search_trends_beaus_lines': tf.float64,
    'search_trends_bells_palsy': tf.float64,
    'search_trends_biliary_colic': tf.float64,
    'search_trends_binge_eating': tf.float64,
    'search_trends_bleeding': tf.float64,
    'search_trends_bleeding_on_probing': tf.float64,
    'search_trends_blepharospasm': tf.float64,
    'search_trends_bloating': tf.float64,
    'search_trends_blood_in_stool': tf.float64,
    'search_trends_blurred_vision': tf.float64,
    'search_trends_blushing': tf.float64,
    'search_trends_boil': tf.float64,
    'search_trends_bone_fracture': tf.float64,
    'search_trends_bone_tumor': tf.float64,
    'search_trends_bowel_obstruction': tf.float64,
    'search_trends_bradycardia': tf.float64,
    'search_trends_braxton_hicks_contractions': tf.float64,
    'search_trends_breakthrough_bleeding': tf.float64,
    'search_trends_breast_pain': tf.float64,
    'search_trends_bronchitis': tf.float64,
    'search_trends_bruise': tf.float64,
    'search_trends_bruxism': tf.float64,
    'search_trends_bunion': tf.float64,
    'search_trends_burn': tf.float64,
    'search_trends_burning_chest_pain': tf.float64,
    'search_trends_burning_mouth_syndrome': tf.float64,
    'search_trends_candidiasis': tf.float64,
    'search_trends_canker_sore': tf.float64,
    'search_trends_cardiac_arrest': tf.float64,
    'search_trends_carpal_tunnel_syndrome': tf.float64,
    'search_trends_cataplexy': tf.float64,
    'search_trends_cataract': tf.float64,
    'search_trends_chancre': tf.float64,
    'search_trends_cheilitis': tf.float64,
    'search_trends_chest_pain': tf.float64,
    'search_trends_chills': tf.float64,
    'search_trends_chorea': tf.float64,
    'search_trends_chronic_pain': tf.float64,
    'search_trends_cirrhosis': tf.float64,
    'search_trends_cleft_lip_and_cleft_palate': tf.float64,
    'search_trends_clouding_of_consciousness': tf.float64,
    'search_trends_cluster_headache': tf.float64,
    'search_trends_colitis': tf.float64,
    'search_trends_coma': tf.float64,
    'search_trends_common_cold': tf.float64,
    'search_trends_compulsive_behavior': tf.float64,
    'search_trends_compulsive_hoarding': tf.float64,
    'search_trends_confusion': tf.float64,
    'search_trends_congenital_heart_defect': tf.float64,
    'search_trends_conjunctivitis': tf.float64,
    'search_trends_constipation': tf.float64,
    'search_trends_convulsion': tf.float64,
    'search_trends_cough': tf.float64,
    'search_trends_crackles': tf.float64,
    'search_trends_cramp': tf.float64,
    'search_trends_crepitus': tf.float64,
    'search_trends_croup': tf.float64,
    'search_trends_cyanosis': tf.float64,
    'search_trends_dandruff': tf.float64,
    'search_trends_delayed_onset_muscle_soreness': tf.float64,
    'search_trends_dementia': tf.float64,
    'search_trends_dentin_hypersensitivity': tf.float64,
    'search_trends_depersonalization': tf.float64,
    'search_trends_depression': tf.float64,
    'search_trends_dermatitis': tf.float64,
    'search_trends_desquamation': tf.float64,
    'search_trends_developmental_disability': tf.float64,
    'search_trends_diabetes': tf.float64,
    'search_trends_diabetic_ketoacidosis': tf.float64,
    'search_trends_diarrhea': tf.float64,
    'search_trends_dizziness': tf.float64,
    'search_trends_dry_eye_syndrome': tf.float64,
    'search_trends_dysautonomia': tf.float64,
    'search_trends_dysgeusia': tf.float64,
    'search_trends_dysmenorrhea': tf.float64,
    'search_trends_dyspareunia': tf.float64,
    'search_trends_dysphagia': tf.float64,
    'search_trends_dysphoria': tf.float64,
    'search_trends_dystonia': tf.float64,
    'search_trends_dysuria': tf.float64,
    'search_trends_ear_pain': tf.float64,
    'search_trends_eczema': tf.float64,
    'search_trends_edema': tf.float64,
    'search_trends_encephalitis': tf.float64,
    'search_trends_encephalopathy': tf.float64,
    'search_trends_epidermoid_cyst': tf.float64,
    'search_trends_epilepsy': tf.float64,
    'search_trends_epiphora': tf.float64,
    'search_trends_erectile_dysfunction': tf.float64,
    'search_trends_erythema': tf.float64,
    'search_trends_erythema_chronicum_migrans': tf.float64,
    'search_trends_esophagitis': tf.float64,
    'search_trends_excessive_daytime_sleepiness': tf.float64,
    'search_trends_eye_pain': tf.float64,
    'search_trends_eye_strain': tf.float64,
    'search_trends_facial_nerve_paralysis': tf.float64,
    'search_trends_facial_swelling': tf.float64,
    'search_trends_fasciculation': tf.float64,
    'search_trends_fatigue': tf.float64,
    'search_trends_fatty_liver_disease': tf.float64,
    'search_trends_fecal_incontinence': tf.float64,
    'search_trends_fever': tf.float64,
    'search_trends_fibrillation': tf.float64,
    'search_trends_fibrocystic_breast_changes': tf.float64,
    'search_trends_fibromyalgia': tf.float64,
    'search_trends_flatulence': tf.float64,
    'search_trends_floater': tf.float64,
    'search_trends_focal_seizure': tf.float64,
    'search_trends_folate_deficiency': tf.float64,
    'search_trends_food_craving': tf.float64,
    'search_trends_food_intolerance': tf.float64,
    'search_trends_frequent_urination': tf.float64,
    'search_trends_gastroesophageal_reflux_disease': tf.float64,
    'search_trends_gastroparesis': tf.float64,
    'search_trends_generalized_anxiety_disorder': tf.float64,
    'search_trends_genital_wart': tf.float64,
    'search_trends_gingival_recession': tf.float64,
    'search_trends_gingivitis': tf.float64,
    'search_trends_globus_pharyngis': tf.float64,
    'search_trends_goitre': tf.float64,
    'search_trends_gout': tf.float64,
    'search_trends_grandiosity': tf.float64,
    'search_trends_granuloma': tf.float64,
    'search_trends_guilt': tf.float64,
    'search_trends_hair_loss': tf.float64,
    'search_trends_halitosis': tf.float64,
    'search_trends_hay_fever': tf.float64,
    'search_trends_headache': tf.float64,
    'search_trends_heart_arrhythmia': tf.float64,
    'search_trends_heart_murmur': tf.float64,
    'search_trends_heartburn': tf.float64,
    'search_trends_hematochezia': tf.float64,
    'search_trends_hematoma': tf.float64,
    'search_trends_hematuria': tf.float64,
    'search_trends_hemolysis': tf.float64,
    'search_trends_hemoptysis': tf.float64,
    'search_trends_hemorrhoids': tf.float64,
    'search_trends_hepatic_encephalopathy': tf.float64,
    'search_trends_hepatitis': tf.float64,
    'search_trends_hepatotoxicity': tf.float64,
    'search_trends_hiccup': tf.float64,
    'search_trends_hip_pain': tf.float64,
    'search_trends_hives': tf.float64,
    'search_trends_hot_flash': tf.float64,
    'search_trends_hydrocephalus': tf.float64,
    'search_trends_hypercalcaemia': tf.float64,
    'search_trends_hypercapnia': tf.float64,
    'search_trends_hypercholesterolemia': tf.float64,
    'search_trends_hyperemesis_gravidarum': tf.float64,
    'search_trends_hyperglycemia': tf.float64,
    'search_trends_hyperhidrosis': tf.float64,
    'search_trends_hyperkalemia': tf.float64,
    'search_trends_hyperlipidemia': tf.float64,
    'search_trends_hypermobility': tf.float64,
    'search_trends_hyperpigmentation': tf.float64,
    'search_trends_hypersomnia': tf.float64,
    'search_trends_hypertension': tf.float64,
    'search_trends_hyperthermia': tf.float64,
    'search_trends_hyperthyroidism': tf.float64,
    'search_trends_hypertriglyceridemia': tf.float64,
    'search_trends_hypertrophy': tf.float64,
    'search_trends_hyperventilation': tf.float64,
    'search_trends_hypocalcaemia': tf.float64,
    'search_trends_hypochondriasis': tf.float64,
    'search_trends_hypoglycemia': tf.float64,
    'search_trends_hypogonadism': tf.float64,
    'search_trends_hypokalemia': tf.float64,
    'search_trends_hypomania': tf.float64,
    'search_trends_hyponatremia': tf.float64,
    'search_trends_hypotension': tf.float64,
    'search_trends_hypothyroidism': tf.float64,
    'search_trends_hypoxemia': tf.float64,
    'search_trends_hypoxia': tf.float64,
    'search_trends_impetigo': tf.float64,
    'search_trends_implantation_bleeding': tf.float64,
    'search_trends_impulsivity': tf.float64,
    'search_trends_indigestion': tf.float64,
    'search_trends_infection': tf.float64,
    'search_trends_inflammation': tf.float64,
    'search_trends_inflammatory_bowel_disease': tf.float64,
    'search_trends_ingrown_hair': tf.float64,
    'search_trends_insomnia': tf.float64,
    'search_trends_insulin_resistance': tf.float64,
    'search_trends_intermenstrual_bleeding': tf.float64,
    'search_trends_intracranial_pressure': tf.float64,
    'search_trends_iron_deficiency': tf.float64,
    'search_trends_irregular_menstruation': tf.float64,
    'search_trends_itch': tf.float64,
    'search_trends_jaundice': tf.float64,
    'search_trends_kidney_failure': tf.float64,
    'search_trends_kidney_stone': tf.float64,
    'search_trends_knee_pain': tf.float64,
    'search_trends_kyphosis': tf.float64,
    'search_trends_lactose_intolerance': tf.float64,
    'search_trends_laryngitis': tf.float64,
    'search_trends_leg_cramps': tf.float64,
    'search_trends_lesion': tf.float64,
    'search_trends_leukorrhea': tf.float64,
    'search_trends_lightheadedness': tf.float64,
    'search_trends_low_back_pain': tf.float64,
    'search_trends_low_grade_fever': tf.float64,
    'search_trends_lymphedema': tf.float64,
    'search_trends_major_depressive_disorder': tf.float64,
    'search_trends_malabsorption': tf.float64,
    'search_trends_male_infertility': tf.float64,
    'search_trends_manic_disorder': tf.float64,
    'search_trends_melasma': tf.float64,
    'search_trends_melena': tf.float64,
    'search_trends_meningitis': tf.float64,
    'search_trends_menorrhagia': tf.float64,
    'search_trends_middle_back_pain': tf.float64,
    'search_trends_migraine': tf.float64,
    'search_trends_milium': tf.float64,
    'search_trends_mitral_insufficiency': tf.float64,
    'search_trends_mood_disorder': tf.float64,
    'search_trends_mood_swing': tf.float64,
    'search_trends_morning_sickness': tf.float64,
    'search_trends_motion_sickness': tf.float64,
    'search_trends_mouth_ulcer': tf.float64,
    'search_trends_muscle_atrophy': tf.float64,
    'search_trends_muscle_weakness': tf.float64,
    'search_trends_myalgia': tf.float64,
    'search_trends_mydriasis': tf.float64,
    'search_trends_myocardial_infarction': tf.float64,
    'search_trends_myoclonus': tf.float64,
    'search_trends_nasal_congestion': tf.float64,
    'search_trends_nasal_polyp': tf.float64,
    'search_trends_nausea': tf.float64,
    'search_trends_neck_mass': tf.float64,
    'search_trends_neck_pain': tf.float64,
    'search_trends_neonatal_jaundice': tf.float64,
    'search_trends_nerve_injury': tf.float64,
    'search_trends_neuralgia': tf.float64,
    'search_trends_neutropenia': tf.float64,
    'search_trends_night_sweats': tf.float64,
    'search_trends_night_terror': tf.float64,
    'search_trends_nocturnal_enuresis': tf.float64,
    'search_trends_nodule': tf.float64,
    'search_trends_nosebleed': tf.float64,
    'search_trends_nystagmus': tf.float64,
    'search_trends_obesity': tf.float64,
    'search_trends_onychorrhexis': tf.float64,
    'search_trends_oral_candidiasis': tf.float64,
    'search_trends_orthostatic_hypotension': tf.float64,
    'search_trends_osteopenia': tf.float64,
    'search_trends_osteophyte': tf.float64,
    'search_trends_osteoporosis': tf.float64,
    'search_trends_otitis': tf.float64,
    'search_trends_otitis_externa': tf.float64,
    'search_trends_otitis_media': tf.float64,
    'search_trends_pain': tf.float64,
    'search_trends_palpitations': tf.float64,
    'search_trends_pancreatitis': tf.float64,
    'search_trends_panic_attack': tf.float64,
    'search_trends_papule': tf.float64,
    'search_trends_paranoia': tf.float64,
    'search_trends_paresthesia': tf.float64,
    'search_trends_pelvic_inflammatory_disease': tf.float64,
    'search_trends_pericarditis': tf.float64,
    'search_trends_periodontal_disease': tf.float64,
    'search_trends_periorbital_puffiness': tf.float64,
    'search_trends_peripheral_neuropathy': tf.float64,
    'search_trends_perspiration': tf.float64,
    'search_trends_petechia': tf.float64,
    'search_trends_phlegm': tf.float64,
    'search_trends_photodermatitis': tf.float64,
    'search_trends_photophobia': tf.float64,
    'search_trends_photopsia': tf.float64,
    'search_trends_pleural_effusion': tf.float64,
    'search_trends_pleurisy': tf.float64,
    'search_trends_pneumonia': tf.float64,
    'search_trends_podalgia': tf.float64,
    'search_trends_polycythemia': tf.float64,
    'search_trends_polydipsia': tf.float64,
    'search_trends_polyneuropathy': tf.float64,
    'search_trends_polyuria': tf.float64,
    'search_trends_poor_posture': tf.float64,
    'search_trends_post_nasal_drip': tf.float64,
    'search_trends_postural_orthostatic_tachycardia_syndrome': tf.float64,
    'search_trends_prediabetes': tf.float64,
    'search_trends_proteinuria': tf.float64,
    'search_trends_pruritus_ani': tf.float64,
    'search_trends_psychosis': tf.float64,
    'search_trends_ptosis': tf.float64,
    'search_trends_pulmonary_edema': tf.float64,
    'search_trends_pulmonary_hypertension': tf.float64,
    'search_trends_purpura': tf.float64,
    'search_trends_pus': tf.float64,
    'search_trends_pyelonephritis': tf.float64,
    'search_trends_radiculopathy': tf.float64,
    'search_trends_rectal_pain': tf.float64,
    'search_trends_rectal_prolapse': tf.float64,
    'search_trends_red_eye': tf.float64,
    'search_trends_renal_colic': tf.float64,
    'search_trends_restless_legs_syndrome': tf.float64,
    'search_trends_rheum': tf.float64,
    'search_trends_rhinitis': tf.float64,
    'search_trends_rhinorrhea': tf.float64,
    'search_trends_rosacea': tf.float64,
    'search_trends_round_ligament_pain': tf.float64,
    'search_trends_rumination': tf.float64,
    'search_trends_scar': tf.float64,
    'search_trends_sciatica': tf.float64,
    'search_trends_scoliosis': tf.float64,
    'search_trends_seborrheic_dermatitis': tf.float64,
    'search_trends_self_harm': tf.float64,
    'search_trends_sensitivity_to_sound': tf.float64,
    'search_trends_sexual_dysfunction': tf.float64,
    'search_trends_shallow_breathing': tf.float64,
    'search_trends_sharp_pain': tf.float64,
    'search_trends_shivering': tf.float64,
    'search_trends_shortness_of_breath': tf.float64,
    'search_trends_shyness': tf.float64,
    'search_trends_sinusitis': tf.float64,
    'search_trends_skin_condition': tf.float64,
    'search_trends_skin_rash': tf.float64,
    'search_trends_skin_tag': tf.float64,
    'search_trends_skin_ulcer': tf.float64,
    'search_trends_sleep_apnea': tf.float64,
    'search_trends_sleep_deprivation': tf.float64,
    'search_trends_sleep_disorder': tf.float64,
    'search_trends_snoring': tf.float64,
    'search_trends_sore_throat': tf.float64,
    'search_trends_spasticity': tf.float64,
    'search_trends_splenomegaly': tf.float64,
    'search_trends_sputum': tf.float64,
    'search_trends_stomach_rumble': tf.float64,
    'search_trends_strabismus': tf.float64,
    'search_trends_stretch_marks': tf.float64,
    'search_trends_stridor': tf.float64,
    'search_trends_stroke': tf.float64,
    'search_trends_stuttering': tf.float64,
    'search_trends_subdural_hematoma': tf.float64,
    'search_trends_suicidal_ideation': tf.float64,
    'search_trends_swelling': tf.float64,
    'search_trends_swollen_feet': tf.float64,
    'search_trends_swollen_lymph_nodes': tf.float64,
    'search_trends_syncope': tf.float64,
    'search_trends_tachycardia': tf.float64,
    'search_trends_tachypnea': tf.float64,
    'search_trends_telangiectasia': tf.float64,
    'search_trends_tenderness': tf.float64,
    'search_trends_testicular_pain': tf.float64,
    'search_trends_throat_irritation': tf.float64,
    'search_trends_thrombocytopenia': tf.float64,
    'search_trends_thyroid_nodule': tf.float64,
    'search_trends_tic': tf.float64,
    'search_trends_tinnitus': tf.float64,
    'search_trends_tonsillitis': tf.float64,
    'search_trends_toothache': tf.float64,
    'search_trends_tremor': tf.float64,
    'search_trends_trichoptilosis': tf.float64,
    'search_trends_tumor': tf.float64,
    'search_trends_type_2_diabetes': tf.float64,
    'search_trends_unconsciousness': tf.float64,
    'search_trends_underweight': tf.float64,
    'search_trends_upper_respiratory_tract_infection': tf.float64,
    'search_trends_urethritis': tf.float64,
    'search_trends_urinary_incontinence': tf.float64,
    'search_trends_urinary_tract_infection': tf.float64,
    'search_trends_urinary_urgency': tf.float64,
    'search_trends_uterine_contraction': tf.float64,
    'search_trends_vaginal_bleeding': tf.float64,
    'search_trends_vaginal_discharge': tf.float64,
    'search_trends_vaginitis': tf.float64,
    'search_trends_varicose_veins': tf.float64,
    'search_trends_vasculitis': tf.float64,
    'search_trends_ventricular_fibrillation': tf.float64,
    'search_trends_ventricular_tachycardia': tf.float64,
    'search_trends_vertigo': tf.float64,
    'search_trends_viral_pneumonia': tf.float64,
    'search_trends_visual_acuity': tf.float64,
    'search_trends_vomiting': tf.float64,
    'search_trends_wart': tf.float64,
    'search_trends_water_retention': tf.float64,
    'search_trends_weakness': tf.float64,
    'search_trends_weight_gain': tf.float64,
    'search_trends_wheeze': tf.float64,
    'search_trends_xeroderma': tf.float64,
    'search_trends_xerostomia': tf.float64,
    'search_trends_yawn': tf.float64,
    'smoking_prevalence': tf.float64,
    'snowfall_mm': tf.float64,
    'stay_at_home_requirements': tf.float64,
    'stringency_index': tf.float64,
    'subregion1_code': tf.string,
    'subregion1_name': tf.string,
    'subregion2_code': tf.string,
    'subregion2_name': tf.string,
    'testing_policy': tf.float64,
    'vaccination_policy': tf.float64,
    'wikidata_id': tf.string,
    'workplace_closing': tf.float64,
})
```

*   **Feature documentation**:

Feature                                                 | Class        | Shape | Dtype      | Description
:------------------------------------------------------ | :----------- | :---- | :--------- | :----------
                                                        | FeaturesDict |       |            |
adult_female_mortality_rate                             | Tensor       |       | tf.float64 |
adult_male_mortality_rate                               | Tensor       |       | tf.float64 |
age_bin_0                                               | Tensor       |       | tf.string  |
age_bin_1                                               | Tensor       |       | tf.string  |
age_bin_2                                               | Tensor       |       | tf.string  |
age_bin_3                                               | Tensor       |       | tf.string  |
age_bin_4                                               | Tensor       |       | tf.string  |
age_bin_5                                               | Tensor       |       | tf.string  |
age_bin_6                                               | Tensor       |       | tf.string  |
age_bin_7                                               | Tensor       |       | tf.string  |
age_bin_8                                               | Tensor       |       | tf.string  |
age_bin_9                                               | Tensor       |       | tf.string  |
aggregation_level                                       | Tensor       |       | tf.float64 |
area_rural_sq_km                                        | Tensor       |       | tf.float64 |
area_sq_km                                              | Tensor       |       | tf.float64 |
area_urban_sq_km                                        | Tensor       |       | tf.float64 |
average_temperature_celsius                             | Tensor       |       | tf.float64 |
cancel_public_events                                    | Tensor       |       | tf.float64 |
comorbidity_mortality_rate                              | Tensor       |       | tf.float64 |
contact_tracing                                         | Tensor       |       | tf.float64 |
country_code                                            | Tensor       |       | tf.string  |
country_name                                            | Tensor       |       | tf.string  |
cumulative_confirmed                                    | Tensor       |       | tf.float64 |
cumulative_confirmed_age_0                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_1                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_2                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_3                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_4                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_5                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_6                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_7                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_8                              | Tensor       |       | tf.float64 |
cumulative_confirmed_age_9                              | Tensor       |       | tf.float64 |
cumulative_confirmed_female                             | Tensor       |       | tf.float64 |
cumulative_confirmed_male                               | Tensor       |       | tf.float64 |
cumulative_deceased                                     | Tensor       |       | tf.float64 |
cumulative_deceased_age_0                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_1                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_2                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_3                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_4                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_5                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_6                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_7                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_8                               | Tensor       |       | tf.float64 |
cumulative_deceased_age_9                               | Tensor       |       | tf.float64 |
cumulative_deceased_female                              | Tensor       |       | tf.float64 |
cumulative_deceased_male                                | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients                        | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_0                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_1                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_2                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_3                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_4                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_5                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_6                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_7                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_8                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_age_9                  | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_female                 | Tensor       |       | tf.float64 |
cumulative_hospitalized_patients_male                   | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients                      | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_0                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_1                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_2                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_3                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_4                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_5                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_6                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_7                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_8                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_age_9                | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_female               | Tensor       |       | tf.float64 |
cumulative_intensive_care_patients_male                 | Tensor       |       | tf.float64 |
cumulative_persons_fully_vaccinated                     | Tensor       |       | tf.float64 |
cumulative_persons_fully_vaccinated_janssen             | Tensor       |       | tf.float64 |
cumulative_persons_fully_vaccinated_moderna             | Tensor       |       | tf.float64 |
cumulative_persons_fully_vaccinated_pfizer              | Tensor       |       | tf.float64 |
cumulative_persons_vaccinated                           | Tensor       |       | tf.float64 |
cumulative_recovered                                    | Tensor       |       | tf.float64 |
cumulative_recovered_age_0                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_1                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_2                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_3                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_4                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_5                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_6                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_7                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_8                              | Tensor       |       | tf.float64 |
cumulative_recovered_age_9                              | Tensor       |       | tf.float64 |
cumulative_recovered_female                             | Tensor       |       | tf.float64 |
cumulative_recovered_male                               | Tensor       |       | tf.float64 |
cumulative_tested                                       | Tensor       |       | tf.float64 |
cumulative_tested_age_0                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_1                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_2                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_3                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_4                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_5                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_6                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_7                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_8                                 | Tensor       |       | tf.float64 |
cumulative_tested_age_9                                 | Tensor       |       | tf.float64 |
cumulative_tested_female                                | Tensor       |       | tf.float64 |
cumulative_tested_male                                  | Tensor       |       | tf.float64 |
cumulative_vaccine_doses_administered                   | Tensor       |       | tf.float64 |
cumulative_vaccine_doses_administered_janssen           | Tensor       |       | tf.float64 |
cumulative_vaccine_doses_administered_moderna           | Tensor       |       | tf.float64 |
cumulative_vaccine_doses_administered_pfizer            | Tensor       |       | tf.float64 |
cumulative_ventilator_patients                          | Tensor       |       | tf.float64 |
current_hospitalized_patients                           | Tensor       |       | tf.float64 |
current_intensive_care_patients                         | Tensor       |       | tf.float64 |
current_ventilator_patients                             | Tensor       |       | tf.float64 |
datacommons_id                                          | Tensor       |       | tf.string  |
date                                                    | Tensor       |       | tf.string  |
debt_relief                                             | Tensor       |       | tf.float64 |
dew_point                                               | Tensor       |       | tf.float64 |
diabetes_prevalence                                     | Tensor       |       | tf.float64 |
elevation_m                                             | Tensor       |       | tf.float64 |
emergency_investment_in_healthcare                      | Tensor       |       | tf.float64 |
facial_coverings                                        | Tensor       |       | tf.float64 |
fiscal_measures                                         | Tensor       |       | tf.float64 |
gdp_per_capita_usd                                      | Tensor       |       | tf.float64 |
gdp_usd                                                 | Tensor       |       | tf.float64 |
health_expenditure_usd                                  | Tensor       |       | tf.float64 |
hospital_beds_per_1000                                  | Tensor       |       | tf.float64 |
human_capital_index                                     | Tensor       |       | tf.float64 |
human_development_index                                 | Tensor       |       | tf.float64 |
income_support                                          | Tensor       |       | tf.float64 |
infant_mortality_rate                                   | Tensor       |       | tf.float64 |
international_support                                   | Tensor       |       | tf.float64 |
international_travel_controls                           | Tensor       |       | tf.float64 |
investment_in_vaccines                                  | Tensor       |       | tf.float64 |
iso_3166_1_alpha_2                                      | Tensor       |       | tf.string  |
iso_3166_1_alpha_3                                      | Tensor       |       | tf.string  |
latitude                                                | Tensor       |       | tf.float64 |
life_expectancy                                         | Tensor       |       | tf.float64 |
locality_code                                           | Tensor       |       | tf.string  |
locality_name                                           | Tensor       |       | tf.string  |
location_key                                            | Tensor       |       | tf.string  |
longitude                                               | Tensor       |       | tf.float64 |
maximum_temperature_celsius                             | Tensor       |       | tf.float64 |
minimum_temperature_celsius                             | Tensor       |       | tf.float64 |
mobility_grocery_and_pharmacy                           | Tensor       |       | tf.float64 |
mobility_parks                                          | Tensor       |       | tf.float64 |
mobility_residential                                    | Tensor       |       | tf.float64 |
mobility_retail_and_recreation                          | Tensor       |       | tf.float64 |
mobility_transit_stations                               | Tensor       |       | tf.float64 |
mobility_workplaces                                     | Tensor       |       | tf.float64 |
new_confirmed                                           | Tensor       |       | tf.float64 |
new_confirmed_age_0                                     | Tensor       |       | tf.float64 |
new_confirmed_age_1                                     | Tensor       |       | tf.float64 |
new_confirmed_age_2                                     | Tensor       |       | tf.float64 |
new_confirmed_age_3                                     | Tensor       |       | tf.float64 |
new_confirmed_age_4                                     | Tensor       |       | tf.float64 |
new_confirmed_age_5                                     | Tensor       |       | tf.float64 |
new_confirmed_age_6                                     | Tensor       |       | tf.float64 |
new_confirmed_age_7                                     | Tensor       |       | tf.float64 |
new_confirmed_age_8                                     | Tensor       |       | tf.float64 |
new_confirmed_age_9                                     | Tensor       |       | tf.float64 |
new_confirmed_female                                    | Tensor       |       | tf.float64 |
new_confirmed_male                                      | Tensor       |       | tf.float64 |
new_deceased                                            | Tensor       |       | tf.float64 |
new_deceased_age_0                                      | Tensor       |       | tf.float64 |
new_deceased_age_1                                      | Tensor       |       | tf.float64 |
new_deceased_age_2                                      | Tensor       |       | tf.float64 |
new_deceased_age_3                                      | Tensor       |       | tf.float64 |
new_deceased_age_4                                      | Tensor       |       | tf.float64 |
new_deceased_age_5                                      | Tensor       |       | tf.float64 |
new_deceased_age_6                                      | Tensor       |       | tf.float64 |
new_deceased_age_7                                      | Tensor       |       | tf.float64 |
new_deceased_age_8                                      | Tensor       |       | tf.float64 |
new_deceased_age_9                                      | Tensor       |       | tf.float64 |
new_deceased_female                                     | Tensor       |       | tf.float64 |
new_deceased_male                                       | Tensor       |       | tf.float64 |
new_hospitalized_patients                               | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_0                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_1                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_2                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_3                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_4                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_5                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_6                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_7                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_8                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_age_9                         | Tensor       |       | tf.float64 |
new_hospitalized_patients_female                        | Tensor       |       | tf.float64 |
new_hospitalized_patients_male                          | Tensor       |       | tf.float64 |
new_intensive_care_patients                             | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_0                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_1                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_2                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_3                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_4                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_5                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_6                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_7                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_8                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_age_9                       | Tensor       |       | tf.float64 |
new_intensive_care_patients_female                      | Tensor       |       | tf.float64 |
new_intensive_care_patients_male                        | Tensor       |       | tf.float64 |
new_persons_fully_vaccinated                            | Tensor       |       | tf.float64 |
new_persons_fully_vaccinated_janssen                    | Tensor       |       | tf.float64 |
new_persons_fully_vaccinated_moderna                    | Tensor       |       | tf.float64 |
new_persons_fully_vaccinated_pfizer                     | Tensor       |       | tf.float64 |
new_persons_vaccinated                                  | Tensor       |       | tf.float64 |
new_recovered                                           | Tensor       |       | tf.float64 |
new_recovered_age_0                                     | Tensor       |       | tf.float64 |
new_recovered_age_1                                     | Tensor       |       | tf.float64 |
new_recovered_age_2                                     | Tensor       |       | tf.float64 |
new_recovered_age_3                                     | Tensor       |       | tf.float64 |
new_recovered_age_4                                     | Tensor       |       | tf.float64 |
new_recovered_age_5                                     | Tensor       |       | tf.float64 |
new_recovered_age_6                                     | Tensor       |       | tf.float64 |
new_recovered_age_7                                     | Tensor       |       | tf.float64 |
new_recovered_age_8                                     | Tensor       |       | tf.float64 |
new_recovered_age_9                                     | Tensor       |       | tf.float64 |
new_recovered_female                                    | Tensor       |       | tf.float64 |
new_recovered_male                                      | Tensor       |       | tf.float64 |
new_tested                                              | Tensor       |       | tf.float64 |
new_tested_age_0                                        | Tensor       |       | tf.float64 |
new_tested_age_1                                        | Tensor       |       | tf.float64 |
new_tested_age_2                                        | Tensor       |       | tf.float64 |
new_tested_age_3                                        | Tensor       |       | tf.float64 |
new_tested_age_4                                        | Tensor       |       | tf.float64 |
new_tested_age_5                                        | Tensor       |       | tf.float64 |
new_tested_age_6                                        | Tensor       |       | tf.float64 |
new_tested_age_7                                        | Tensor       |       | tf.float64 |
new_tested_age_8                                        | Tensor       |       | tf.float64 |
new_tested_age_9                                        | Tensor       |       | tf.float64 |
new_tested_female                                       | Tensor       |       | tf.float64 |
new_tested_male                                         | Tensor       |       | tf.float64 |
new_vaccine_doses_administered                          | Tensor       |       | tf.float64 |
new_vaccine_doses_administered_janssen                  | Tensor       |       | tf.float64 |
new_vaccine_doses_administered_moderna                  | Tensor       |       | tf.float64 |
new_vaccine_doses_administered_pfizer                   | Tensor       |       | tf.float64 |
new_ventilator_patients                                 | Tensor       |       | tf.float64 |
nurses_per_1000                                         | Tensor       |       | tf.float64 |
openstreetmap_id                                        | Tensor       |       | tf.string  |
out_of_pocket_health_expenditure_usd                    | Tensor       |       | tf.float64 |
physicians_per_1000                                     | Tensor       |       | tf.float64 |
place_id                                                | Tensor       |       | tf.string  |
pollution_mortality_rate                                | Tensor       |       | tf.float64 |
population                                              | Tensor       |       | tf.float64 |
population_age_00_09                                    | Tensor       |       | tf.float64 |
population_age_10_19                                    | Tensor       |       | tf.float64 |
population_age_20_29                                    | Tensor       |       | tf.float64 |
population_age_30_39                                    | Tensor       |       | tf.float64 |
population_age_40_49                                    | Tensor       |       | tf.float64 |
population_age_50_59                                    | Tensor       |       | tf.float64 |
population_age_60_69                                    | Tensor       |       | tf.float64 |
population_age_70_79                                    | Tensor       |       | tf.float64 |
population_age_80_and_older                             | Tensor       |       | tf.float64 |
population_clustered                                    | Tensor       |       | tf.float64 |
population_density                                      | Tensor       |       | tf.float64 |
population_female                                       | Tensor       |       | tf.float64 |
population_largest_city                                 | Tensor       |       | tf.float64 |
population_male                                         | Tensor       |       | tf.float64 |
population_rural                                        | Tensor       |       | tf.float64 |
population_urban                                        | Tensor       |       | tf.float64 |
public_information_campaigns                            | Tensor       |       | tf.float64 |
public_transport_closing                                | Tensor       |       | tf.float64 |
rainfall_mm                                             | Tensor       |       | tf.float64 |
relative_humidity                                       | Tensor       |       | tf.float64 |
restrictions_on_gatherings                              | Tensor       |       | tf.float64 |
restrictions_on_internal_movement                       | Tensor       |       | tf.float64 |
school_closing                                          | Tensor       |       | tf.float64 |
search_trends_abdominal_obesity                         | Tensor       |       | tf.float64 |
search_trends_abdominal_pain                            | Tensor       |       | tf.float64 |
search_trends_acne                                      | Tensor       |       | tf.float64 |
search_trends_actinic_keratosis                         | Tensor       |       | tf.float64 |
search_trends_acute_bronchitis                          | Tensor       |       | tf.float64 |
search_trends_adrenal_crisis                            | Tensor       |       | tf.float64 |
search_trends_ageusia                                   | Tensor       |       | tf.float64 |
search_trends_alcoholism                                | Tensor       |       | tf.float64 |
search_trends_allergic_conjunctivitis                   | Tensor       |       | tf.float64 |
search_trends_allergy                                   | Tensor       |       | tf.float64 |
search_trends_amblyopia                                 | Tensor       |       | tf.float64 |
search_trends_amenorrhea                                | Tensor       |       | tf.float64 |
search_trends_amnesia                                   | Tensor       |       | tf.float64 |
search_trends_anal_fissure                              | Tensor       |       | tf.float64 |
search_trends_anaphylaxis                               | Tensor       |       | tf.float64 |
search_trends_anemia                                    | Tensor       |       | tf.float64 |
search_trends_angina_pectoris                           | Tensor       |       | tf.float64 |
search_trends_angioedema                                | Tensor       |       | tf.float64 |
search_trends_angular_cheilitis                         | Tensor       |       | tf.float64 |
search_trends_anosmia                                   | Tensor       |       | tf.float64 |
search_trends_anxiety                                   | Tensor       |       | tf.float64 |
search_trends_aphasia                                   | Tensor       |       | tf.float64 |
search_trends_aphonia                                   | Tensor       |       | tf.float64 |
search_trends_apnea                                     | Tensor       |       | tf.float64 |
search_trends_arthralgia                                | Tensor       |       | tf.float64 |
search_trends_arthritis                                 | Tensor       |       | tf.float64 |
search_trends_ascites                                   | Tensor       |       | tf.float64 |
search_trends_asperger_syndrome                         | Tensor       |       | tf.float64 |
search_trends_asphyxia                                  | Tensor       |       | tf.float64 |
search_trends_asthma                                    | Tensor       |       | tf.float64 |
search_trends_astigmatism                               | Tensor       |       | tf.float64 |
search_trends_ataxia                                    | Tensor       |       | tf.float64 |
search_trends_atheroma                                  | Tensor       |       | tf.float64 |
search_trends_attention_deficit_hyperactivity_disorder  | Tensor       |       | tf.float64 |
search_trends_auditory_hallucination                    | Tensor       |       | tf.float64 |
search_trends_autoimmune_disease                        | Tensor       |       | tf.float64 |
search_trends_avoidant_personality_disorder             | Tensor       |       | tf.float64 |
search_trends_back_pain                                 | Tensor       |       | tf.float64 |
search_trends_bacterial_vaginosis                       | Tensor       |       | tf.float64 |
search_trends_balance_disorder                          | Tensor       |       | tf.float64 |
search_trends_beaus_lines                               | Tensor       |       | tf.float64 |
search_trends_bells_palsy                               | Tensor       |       | tf.float64 |
search_trends_biliary_colic                             | Tensor       |       | tf.float64 |
search_trends_binge_eating                              | Tensor       |       | tf.float64 |
search_trends_bleeding                                  | Tensor       |       | tf.float64 |
search_trends_bleeding_on_probing                       | Tensor       |       | tf.float64 |
search_trends_blepharospasm                             | Tensor       |       | tf.float64 |
search_trends_bloating                                  | Tensor       |       | tf.float64 |
search_trends_blood_in_stool                            | Tensor       |       | tf.float64 |
search_trends_blurred_vision                            | Tensor       |       | tf.float64 |
search_trends_blushing                                  | Tensor       |       | tf.float64 |
search_trends_boil                                      | Tensor       |       | tf.float64 |
search_trends_bone_fracture                             | Tensor       |       | tf.float64 |
search_trends_bone_tumor                                | Tensor       |       | tf.float64 |
search_trends_bowel_obstruction                         | Tensor       |       | tf.float64 |
search_trends_bradycardia                               | Tensor       |       | tf.float64 |
search_trends_braxton_hicks_contractions                | Tensor       |       | tf.float64 |
search_trends_breakthrough_bleeding                     | Tensor       |       | tf.float64 |
search_trends_breast_pain                               | Tensor       |       | tf.float64 |
search_trends_bronchitis                                | Tensor       |       | tf.float64 |
search_trends_bruise                                    | Tensor       |       | tf.float64 |
search_trends_bruxism                                   | Tensor       |       | tf.float64 |
search_trends_bunion                                    | Tensor       |       | tf.float64 |
search_trends_burn                                      | Tensor       |       | tf.float64 |
search_trends_burning_chest_pain                        | Tensor       |       | tf.float64 |
search_trends_burning_mouth_syndrome                    | Tensor       |       | tf.float64 |
search_trends_candidiasis                               | Tensor       |       | tf.float64 |
search_trends_canker_sore                               | Tensor       |       | tf.float64 |
search_trends_cardiac_arrest                            | Tensor       |       | tf.float64 |
search_trends_carpal_tunnel_syndrome                    | Tensor       |       | tf.float64 |
search_trends_cataplexy                                 | Tensor       |       | tf.float64 |
search_trends_cataract                                  | Tensor       |       | tf.float64 |
search_trends_chancre                                   | Tensor       |       | tf.float64 |
search_trends_cheilitis                                 | Tensor       |       | tf.float64 |
search_trends_chest_pain                                | Tensor       |       | tf.float64 |
search_trends_chills                                    | Tensor       |       | tf.float64 |
search_trends_chorea                                    | Tensor       |       | tf.float64 |
search_trends_chronic_pain                              | Tensor       |       | tf.float64 |
search_trends_cirrhosis                                 | Tensor       |       | tf.float64 |
search_trends_cleft_lip_and_cleft_palate                | Tensor       |       | tf.float64 |
search_trends_clouding_of_consciousness                 | Tensor       |       | tf.float64 |
search_trends_cluster_headache                          | Tensor       |       | tf.float64 |
search_trends_colitis                                   | Tensor       |       | tf.float64 |
search_trends_coma                                      | Tensor       |       | tf.float64 |
search_trends_common_cold                               | Tensor       |       | tf.float64 |
search_trends_compulsive_behavior                       | Tensor       |       | tf.float64 |
search_trends_compulsive_hoarding                       | Tensor       |       | tf.float64 |
search_trends_confusion                                 | Tensor       |       | tf.float64 |
search_trends_congenital_heart_defect                   | Tensor       |       | tf.float64 |
search_trends_conjunctivitis                            | Tensor       |       | tf.float64 |
search_trends_constipation                              | Tensor       |       | tf.float64 |
search_trends_convulsion                                | Tensor       |       | tf.float64 |
search_trends_cough                                     | Tensor       |       | tf.float64 |
search_trends_crackles                                  | Tensor       |       | tf.float64 |
search_trends_cramp                                     | Tensor       |       | tf.float64 |
search_trends_crepitus                                  | Tensor       |       | tf.float64 |
search_trends_croup                                     | Tensor       |       | tf.float64 |
search_trends_cyanosis                                  | Tensor       |       | tf.float64 |
search_trends_dandruff                                  | Tensor       |       | tf.float64 |
search_trends_delayed_onset_muscle_soreness             | Tensor       |       | tf.float64 |
search_trends_dementia                                  | Tensor       |       | tf.float64 |
search_trends_dentin_hypersensitivity                   | Tensor       |       | tf.float64 |
search_trends_depersonalization                         | Tensor       |       | tf.float64 |
search_trends_depression                                | Tensor       |       | tf.float64 |
search_trends_dermatitis                                | Tensor       |       | tf.float64 |
search_trends_desquamation                              | Tensor       |       | tf.float64 |
search_trends_developmental_disability                  | Tensor       |       | tf.float64 |
search_trends_diabetes                                  | Tensor       |       | tf.float64 |
search_trends_diabetic_ketoacidosis                     | Tensor       |       | tf.float64 |
search_trends_diarrhea                                  | Tensor       |       | tf.float64 |
search_trends_dizziness                                 | Tensor       |       | tf.float64 |
search_trends_dry_eye_syndrome                          | Tensor       |       | tf.float64 |
search_trends_dysautonomia                              | Tensor       |       | tf.float64 |
search_trends_dysgeusia                                 | Tensor       |       | tf.float64 |
search_trends_dysmenorrhea                              | Tensor       |       | tf.float64 |
search_trends_dyspareunia                               | Tensor       |       | tf.float64 |
search_trends_dysphagia                                 | Tensor       |       | tf.float64 |
search_trends_dysphoria                                 | Tensor       |       | tf.float64 |
search_trends_dystonia                                  | Tensor       |       | tf.float64 |
search_trends_dysuria                                   | Tensor       |       | tf.float64 |
search_trends_ear_pain                                  | Tensor       |       | tf.float64 |
search_trends_eczema                                    | Tensor       |       | tf.float64 |
search_trends_edema                                     | Tensor       |       | tf.float64 |
search_trends_encephalitis                              | Tensor       |       | tf.float64 |
search_trends_encephalopathy                            | Tensor       |       | tf.float64 |
search_trends_epidermoid_cyst                           | Tensor       |       | tf.float64 |
search_trends_epilepsy                                  | Tensor       |       | tf.float64 |
search_trends_epiphora                                  | Tensor       |       | tf.float64 |
search_trends_erectile_dysfunction                      | Tensor       |       | tf.float64 |
search_trends_erythema                                  | Tensor       |       | tf.float64 |
search_trends_erythema_chronicum_migrans                | Tensor       |       | tf.float64 |
search_trends_esophagitis                               | Tensor       |       | tf.float64 |
search_trends_excessive_daytime_sleepiness              | Tensor       |       | tf.float64 |
search_trends_eye_pain                                  | Tensor       |       | tf.float64 |
search_trends_eye_strain                                | Tensor       |       | tf.float64 |
search_trends_facial_nerve_paralysis                    | Tensor       |       | tf.float64 |
search_trends_facial_swelling                           | Tensor       |       | tf.float64 |
search_trends_fasciculation                             | Tensor       |       | tf.float64 |
search_trends_fatigue                                   | Tensor       |       | tf.float64 |
search_trends_fatty_liver_disease                       | Tensor       |       | tf.float64 |
search_trends_fecal_incontinence                        | Tensor       |       | tf.float64 |
search_trends_fever                                     | Tensor       |       | tf.float64 |
search_trends_fibrillation                              | Tensor       |       | tf.float64 |
search_trends_fibrocystic_breast_changes                | Tensor       |       | tf.float64 |
search_trends_fibromyalgia                              | Tensor       |       | tf.float64 |
search_trends_flatulence                                | Tensor       |       | tf.float64 |
search_trends_floater                                   | Tensor       |       | tf.float64 |
search_trends_focal_seizure                             | Tensor       |       | tf.float64 |
search_trends_folate_deficiency                         | Tensor       |       | tf.float64 |
search_trends_food_craving                              | Tensor       |       | tf.float64 |
search_trends_food_intolerance                          | Tensor       |       | tf.float64 |
search_trends_frequent_urination                        | Tensor       |       | tf.float64 |
search_trends_gastroesophageal_reflux_disease           | Tensor       |       | tf.float64 |
search_trends_gastroparesis                             | Tensor       |       | tf.float64 |
search_trends_generalized_anxiety_disorder              | Tensor       |       | tf.float64 |
search_trends_genital_wart                              | Tensor       |       | tf.float64 |
search_trends_gingival_recession                        | Tensor       |       | tf.float64 |
search_trends_gingivitis                                | Tensor       |       | tf.float64 |
search_trends_globus_pharyngis                          | Tensor       |       | tf.float64 |
search_trends_goitre                                    | Tensor       |       | tf.float64 |
search_trends_gout                                      | Tensor       |       | tf.float64 |
search_trends_grandiosity                               | Tensor       |       | tf.float64 |
search_trends_granuloma                                 | Tensor       |       | tf.float64 |
search_trends_guilt                                     | Tensor       |       | tf.float64 |
search_trends_hair_loss                                 | Tensor       |       | tf.float64 |
search_trends_halitosis                                 | Tensor       |       | tf.float64 |
search_trends_hay_fever                                 | Tensor       |       | tf.float64 |
search_trends_headache                                  | Tensor       |       | tf.float64 |
search_trends_heart_arrhythmia                          | Tensor       |       | tf.float64 |
search_trends_heart_murmur                              | Tensor       |       | tf.float64 |
search_trends_heartburn                                 | Tensor       |       | tf.float64 |
search_trends_hematochezia                              | Tensor       |       | tf.float64 |
search_trends_hematoma                                  | Tensor       |       | tf.float64 |
search_trends_hematuria                                 | Tensor       |       | tf.float64 |
search_trends_hemolysis                                 | Tensor       |       | tf.float64 |
search_trends_hemoptysis                                | Tensor       |       | tf.float64 |
search_trends_hemorrhoids                               | Tensor       |       | tf.float64 |
search_trends_hepatic_encephalopathy                    | Tensor       |       | tf.float64 |
search_trends_hepatitis                                 | Tensor       |       | tf.float64 |
search_trends_hepatotoxicity                            | Tensor       |       | tf.float64 |
search_trends_hiccup                                    | Tensor       |       | tf.float64 |
search_trends_hip_pain                                  | Tensor       |       | tf.float64 |
search_trends_hives                                     | Tensor       |       | tf.float64 |
search_trends_hot_flash                                 | Tensor       |       | tf.float64 |
search_trends_hydrocephalus                             | Tensor       |       | tf.float64 |
search_trends_hypercalcaemia                            | Tensor       |       | tf.float64 |
search_trends_hypercapnia                               | Tensor       |       | tf.float64 |
search_trends_hypercholesterolemia                      | Tensor       |       | tf.float64 |
search_trends_hyperemesis_gravidarum                    | Tensor       |       | tf.float64 |
search_trends_hyperglycemia                             | Tensor       |       | tf.float64 |
search_trends_hyperhidrosis                             | Tensor       |       | tf.float64 |
search_trends_hyperkalemia                              | Tensor       |       | tf.float64 |
search_trends_hyperlipidemia                            | Tensor       |       | tf.float64 |
search_trends_hypermobility                             | Tensor       |       | tf.float64 |
search_trends_hyperpigmentation                         | Tensor       |       | tf.float64 |
search_trends_hypersomnia                               | Tensor       |       | tf.float64 |
search_trends_hypertension                              | Tensor       |       | tf.float64 |
search_trends_hyperthermia                              | Tensor       |       | tf.float64 |
search_trends_hyperthyroidism                           | Tensor       |       | tf.float64 |
search_trends_hypertriglyceridemia                      | Tensor       |       | tf.float64 |
search_trends_hypertrophy                               | Tensor       |       | tf.float64 |
search_trends_hyperventilation                          | Tensor       |       | tf.float64 |
search_trends_hypocalcaemia                             | Tensor       |       | tf.float64 |
search_trends_hypochondriasis                           | Tensor       |       | tf.float64 |
search_trends_hypoglycemia                              | Tensor       |       | tf.float64 |
search_trends_hypogonadism                              | Tensor       |       | tf.float64 |
search_trends_hypokalemia                               | Tensor       |       | tf.float64 |
search_trends_hypomania                                 | Tensor       |       | tf.float64 |
search_trends_hyponatremia                              | Tensor       |       | tf.float64 |
search_trends_hypotension                               | Tensor       |       | tf.float64 |
search_trends_hypothyroidism                            | Tensor       |       | tf.float64 |
search_trends_hypoxemia                                 | Tensor       |       | tf.float64 |
search_trends_hypoxia                                   | Tensor       |       | tf.float64 |
search_trends_impetigo                                  | Tensor       |       | tf.float64 |
search_trends_implantation_bleeding                     | Tensor       |       | tf.float64 |
search_trends_impulsivity                               | Tensor       |       | tf.float64 |
search_trends_indigestion                               | Tensor       |       | tf.float64 |
search_trends_infection                                 | Tensor       |       | tf.float64 |
search_trends_inflammation                              | Tensor       |       | tf.float64 |
search_trends_inflammatory_bowel_disease                | Tensor       |       | tf.float64 |
search_trends_ingrown_hair                              | Tensor       |       | tf.float64 |
search_trends_insomnia                                  | Tensor       |       | tf.float64 |
search_trends_insulin_resistance                        | Tensor       |       | tf.float64 |
search_trends_intermenstrual_bleeding                   | Tensor       |       | tf.float64 |
search_trends_intracranial_pressure                     | Tensor       |       | tf.float64 |
search_trends_iron_deficiency                           | Tensor       |       | tf.float64 |
search_trends_irregular_menstruation                    | Tensor       |       | tf.float64 |
search_trends_itch                                      | Tensor       |       | tf.float64 |
search_trends_jaundice                                  | Tensor       |       | tf.float64 |
search_trends_kidney_failure                            | Tensor       |       | tf.float64 |
search_trends_kidney_stone                              | Tensor       |       | tf.float64 |
search_trends_knee_pain                                 | Tensor       |       | tf.float64 |
search_trends_kyphosis                                  | Tensor       |       | tf.float64 |
search_trends_lactose_intolerance                       | Tensor       |       | tf.float64 |
search_trends_laryngitis                                | Tensor       |       | tf.float64 |
search_trends_leg_cramps                                | Tensor       |       | tf.float64 |
search_trends_lesion                                    | Tensor       |       | tf.float64 |
search_trends_leukorrhea                                | Tensor       |       | tf.float64 |
search_trends_lightheadedness                           | Tensor       |       | tf.float64 |
search_trends_low_back_pain                             | Tensor       |       | tf.float64 |
search_trends_low_grade_fever                           | Tensor       |       | tf.float64 |
search_trends_lymphedema                                | Tensor       |       | tf.float64 |
search_trends_major_depressive_disorder                 | Tensor       |       | tf.float64 |
search_trends_malabsorption                             | Tensor       |       | tf.float64 |
search_trends_male_infertility                          | Tensor       |       | tf.float64 |
search_trends_manic_disorder                            | Tensor       |       | tf.float64 |
search_trends_melasma                                   | Tensor       |       | tf.float64 |
search_trends_melena                                    | Tensor       |       | tf.float64 |
search_trends_meningitis                                | Tensor       |       | tf.float64 |
search_trends_menorrhagia                               | Tensor       |       | tf.float64 |
search_trends_middle_back_pain                          | Tensor       |       | tf.float64 |
search_trends_migraine                                  | Tensor       |       | tf.float64 |
search_trends_milium                                    | Tensor       |       | tf.float64 |
search_trends_mitral_insufficiency                      | Tensor       |       | tf.float64 |
search_trends_mood_disorder                             | Tensor       |       | tf.float64 |
search_trends_mood_swing                                | Tensor       |       | tf.float64 |
search_trends_morning_sickness                          | Tensor       |       | tf.float64 |
search_trends_motion_sickness                           | Tensor       |       | tf.float64 |
search_trends_mouth_ulcer                               | Tensor       |       | tf.float64 |
search_trends_muscle_atrophy                            | Tensor       |       | tf.float64 |
search_trends_muscle_weakness                           | Tensor       |       | tf.float64 |
search_trends_myalgia                                   | Tensor       |       | tf.float64 |
search_trends_mydriasis                                 | Tensor       |       | tf.float64 |
search_trends_myocardial_infarction                     | Tensor       |       | tf.float64 |
search_trends_myoclonus                                 | Tensor       |       | tf.float64 |
search_trends_nasal_congestion                          | Tensor       |       | tf.float64 |
search_trends_nasal_polyp                               | Tensor       |       | tf.float64 |
search_trends_nausea                                    | Tensor       |       | tf.float64 |
search_trends_neck_mass                                 | Tensor       |       | tf.float64 |
search_trends_neck_pain                                 | Tensor       |       | tf.float64 |
search_trends_neonatal_jaundice                         | Tensor       |       | tf.float64 |
search_trends_nerve_injury                              | Tensor       |       | tf.float64 |
search_trends_neuralgia                                 | Tensor       |       | tf.float64 |
search_trends_neutropenia                               | Tensor       |       | tf.float64 |
search_trends_night_sweats                              | Tensor       |       | tf.float64 |
search_trends_night_terror                              | Tensor       |       | tf.float64 |
search_trends_nocturnal_enuresis                        | Tensor       |       | tf.float64 |
search_trends_nodule                                    | Tensor       |       | tf.float64 |
search_trends_nosebleed                                 | Tensor       |       | tf.float64 |
search_trends_nystagmus                                 | Tensor       |       | tf.float64 |
search_trends_obesity                                   | Tensor       |       | tf.float64 |
search_trends_onychorrhexis                             | Tensor       |       | tf.float64 |
search_trends_oral_candidiasis                          | Tensor       |       | tf.float64 |
search_trends_orthostatic_hypotension                   | Tensor       |       | tf.float64 |
search_trends_osteopenia                                | Tensor       |       | tf.float64 |
search_trends_osteophyte                                | Tensor       |       | tf.float64 |
search_trends_osteoporosis                              | Tensor       |       | tf.float64 |
search_trends_otitis                                    | Tensor       |       | tf.float64 |
search_trends_otitis_externa                            | Tensor       |       | tf.float64 |
search_trends_otitis_media                              | Tensor       |       | tf.float64 |
search_trends_pain                                      | Tensor       |       | tf.float64 |
search_trends_palpitations                              | Tensor       |       | tf.float64 |
search_trends_pancreatitis                              | Tensor       |       | tf.float64 |
search_trends_panic_attack                              | Tensor       |       | tf.float64 |
search_trends_papule                                    | Tensor       |       | tf.float64 |
search_trends_paranoia                                  | Tensor       |       | tf.float64 |
search_trends_paresthesia                               | Tensor       |       | tf.float64 |
search_trends_pelvic_inflammatory_disease               | Tensor       |       | tf.float64 |
search_trends_pericarditis                              | Tensor       |       | tf.float64 |
search_trends_periodontal_disease                       | Tensor       |       | tf.float64 |
search_trends_periorbital_puffiness                     | Tensor       |       | tf.float64 |
search_trends_peripheral_neuropathy                     | Tensor       |       | tf.float64 |
search_trends_perspiration                              | Tensor       |       | tf.float64 |
search_trends_petechia                                  | Tensor       |       | tf.float64 |
search_trends_phlegm                                    | Tensor       |       | tf.float64 |
search_trends_photodermatitis                           | Tensor       |       | tf.float64 |
search_trends_photophobia                               | Tensor       |       | tf.float64 |
search_trends_photopsia                                 | Tensor       |       | tf.float64 |
search_trends_pleural_effusion                          | Tensor       |       | tf.float64 |
search_trends_pleurisy                                  | Tensor       |       | tf.float64 |
search_trends_pneumonia                                 | Tensor       |       | tf.float64 |
search_trends_podalgia                                  | Tensor       |       | tf.float64 |
search_trends_polycythemia                              | Tensor       |       | tf.float64 |
search_trends_polydipsia                                | Tensor       |       | tf.float64 |
search_trends_polyneuropathy                            | Tensor       |       | tf.float64 |
search_trends_polyuria                                  | Tensor       |       | tf.float64 |
search_trends_poor_posture                              | Tensor       |       | tf.float64 |
search_trends_post_nasal_drip                           | Tensor       |       | tf.float64 |
search_trends_postural_orthostatic_tachycardia_syndrome | Tensor       |       | tf.float64 |
search_trends_prediabetes                               | Tensor       |       | tf.float64 |
search_trends_proteinuria                               | Tensor       |       | tf.float64 |
search_trends_pruritus_ani                              | Tensor       |       | tf.float64 |
search_trends_psychosis                                 | Tensor       |       | tf.float64 |
search_trends_ptosis                                    | Tensor       |       | tf.float64 |
search_trends_pulmonary_edema                           | Tensor       |       | tf.float64 |
search_trends_pulmonary_hypertension                    | Tensor       |       | tf.float64 |
search_trends_purpura                                   | Tensor       |       | tf.float64 |
search_trends_pus                                       | Tensor       |       | tf.float64 |
search_trends_pyelonephritis                            | Tensor       |       | tf.float64 |
search_trends_radiculopathy                             | Tensor       |       | tf.float64 |
search_trends_rectal_pain                               | Tensor       |       | tf.float64 |
search_trends_rectal_prolapse                           | Tensor       |       | tf.float64 |
search_trends_red_eye                                   | Tensor       |       | tf.float64 |
search_trends_renal_colic                               | Tensor       |       | tf.float64 |
search_trends_restless_legs_syndrome                    | Tensor       |       | tf.float64 |
search_trends_rheum                                     | Tensor       |       | tf.float64 |
search_trends_rhinitis                                  | Tensor       |       | tf.float64 |
search_trends_rhinorrhea                                | Tensor       |       | tf.float64 |
search_trends_rosacea                                   | Tensor       |       | tf.float64 |
search_trends_round_ligament_pain                       | Tensor       |       | tf.float64 |
search_trends_rumination                                | Tensor       |       | tf.float64 |
search_trends_scar                                      | Tensor       |       | tf.float64 |
search_trends_sciatica                                  | Tensor       |       | tf.float64 |
search_trends_scoliosis                                 | Tensor       |       | tf.float64 |
search_trends_seborrheic_dermatitis                     | Tensor       |       | tf.float64 |
search_trends_self_harm                                 | Tensor       |       | tf.float64 |
search_trends_sensitivity_to_sound                      | Tensor       |       | tf.float64 |
search_trends_sexual_dysfunction                        | Tensor       |       | tf.float64 |
search_trends_shallow_breathing                         | Tensor       |       | tf.float64 |
search_trends_sharp_pain                                | Tensor       |       | tf.float64 |
search_trends_shivering                                 | Tensor       |       | tf.float64 |
search_trends_shortness_of_breath                       | Tensor       |       | tf.float64 |
search_trends_shyness                                   | Tensor       |       | tf.float64 |
search_trends_sinusitis                                 | Tensor       |       | tf.float64 |
search_trends_skin_condition                            | Tensor       |       | tf.float64 |
search_trends_skin_rash                                 | Tensor       |       | tf.float64 |
search_trends_skin_tag                                  | Tensor       |       | tf.float64 |
search_trends_skin_ulcer                                | Tensor       |       | tf.float64 |
search_trends_sleep_apnea                               | Tensor       |       | tf.float64 |
search_trends_sleep_deprivation                         | Tensor       |       | tf.float64 |
search_trends_sleep_disorder                            | Tensor       |       | tf.float64 |
search_trends_snoring                                   | Tensor       |       | tf.float64 |
search_trends_sore_throat                               | Tensor       |       | tf.float64 |
search_trends_spasticity                                | Tensor       |       | tf.float64 |
search_trends_splenomegaly                              | Tensor       |       | tf.float64 |
search_trends_sputum                                    | Tensor       |       | tf.float64 |
search_trends_stomach_rumble                            | Tensor       |       | tf.float64 |
search_trends_strabismus                                | Tensor       |       | tf.float64 |
search_trends_stretch_marks                             | Tensor       |       | tf.float64 |
search_trends_stridor                                   | Tensor       |       | tf.float64 |
search_trends_stroke                                    | Tensor       |       | tf.float64 |
search_trends_stuttering                                | Tensor       |       | tf.float64 |
search_trends_subdural_hematoma                         | Tensor       |       | tf.float64 |
search_trends_suicidal_ideation                         | Tensor       |       | tf.float64 |
search_trends_swelling                                  | Tensor       |       | tf.float64 |
search_trends_swollen_feet                              | Tensor       |       | tf.float64 |
search_trends_swollen_lymph_nodes                       | Tensor       |       | tf.float64 |
search_trends_syncope                                   | Tensor       |       | tf.float64 |
search_trends_tachycardia                               | Tensor       |       | tf.float64 |
search_trends_tachypnea                                 | Tensor       |       | tf.float64 |
search_trends_telangiectasia                            | Tensor       |       | tf.float64 |
search_trends_tenderness                                | Tensor       |       | tf.float64 |
search_trends_testicular_pain                           | Tensor       |       | tf.float64 |
search_trends_throat_irritation                         | Tensor       |       | tf.float64 |
search_trends_thrombocytopenia                          | Tensor       |       | tf.float64 |
search_trends_thyroid_nodule                            | Tensor       |       | tf.float64 |
search_trends_tic                                       | Tensor       |       | tf.float64 |
search_trends_tinnitus                                  | Tensor       |       | tf.float64 |
search_trends_tonsillitis                               | Tensor       |       | tf.float64 |
search_trends_toothache                                 | Tensor       |       | tf.float64 |
search_trends_tremor                                    | Tensor       |       | tf.float64 |
search_trends_trichoptilosis                            | Tensor       |       | tf.float64 |
search_trends_tumor                                     | Tensor       |       | tf.float64 |
search_trends_type_2_diabetes                           | Tensor       |       | tf.float64 |
search_trends_unconsciousness                           | Tensor       |       | tf.float64 |
search_trends_underweight                               | Tensor       |       | tf.float64 |
search_trends_upper_respiratory_tract_infection         | Tensor       |       | tf.float64 |
search_trends_urethritis                                | Tensor       |       | tf.float64 |
search_trends_urinary_incontinence                      | Tensor       |       | tf.float64 |
search_trends_urinary_tract_infection                   | Tensor       |       | tf.float64 |
search_trends_urinary_urgency                           | Tensor       |       | tf.float64 |
search_trends_uterine_contraction                       | Tensor       |       | tf.float64 |
search_trends_vaginal_bleeding                          | Tensor       |       | tf.float64 |
search_trends_vaginal_discharge                         | Tensor       |       | tf.float64 |
search_trends_vaginitis                                 | Tensor       |       | tf.float64 |
search_trends_varicose_veins                            | Tensor       |       | tf.float64 |
search_trends_vasculitis                                | Tensor       |       | tf.float64 |
search_trends_ventricular_fibrillation                  | Tensor       |       | tf.float64 |
search_trends_ventricular_tachycardia                   | Tensor       |       | tf.float64 |
search_trends_vertigo                                   | Tensor       |       | tf.float64 |
search_trends_viral_pneumonia                           | Tensor       |       | tf.float64 |
search_trends_visual_acuity                             | Tensor       |       | tf.float64 |
search_trends_vomiting                                  | Tensor       |       | tf.float64 |
search_trends_wart                                      | Tensor       |       | tf.float64 |
search_trends_water_retention                           | Tensor       |       | tf.float64 |
search_trends_weakness                                  | Tensor       |       | tf.float64 |
search_trends_weight_gain                               | Tensor       |       | tf.float64 |
search_trends_wheeze                                    | Tensor       |       | tf.float64 |
search_trends_xeroderma                                 | Tensor       |       | tf.float64 |
search_trends_xerostomia                                | Tensor       |       | tf.float64 |
search_trends_yawn                                      | Tensor       |       | tf.float64 |
smoking_prevalence                                      | Tensor       |       | tf.float64 |
snowfall_mm                                             | Tensor       |       | tf.float64 |
stay_at_home_requirements                               | Tensor       |       | tf.float64 |
stringency_index                                        | Tensor       |       | tf.float64 |
subregion1_code                                         | Tensor       |       | tf.string  |
subregion1_name                                         | Tensor       |       | tf.string  |
subregion2_code                                         | Tensor       |       | tf.string  |
subregion2_name                                         | Tensor       |       | tf.string  |
testing_policy                                          | Tensor       |       | tf.float64 |
vaccination_policy                                      | Tensor       |       | tf.float64 |
wikidata_id                                             | Tensor       |       | tf.string  |
workplace_closing                                       | Tensor       |       | tf.float64 |

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

