disease_dic = {
    'Apta': "<b>Apta</b>: Bauhinia racemosa — Apta is a small deciduous tree native to India, commonly found in dry deciduous forests of Maharashtra, Kerala, and Tamil Nadu. It is revered during the Hindu festival of Dussehra, where its leaves symbolize prosperity. The tree prefers dry tropical climates, thriving in well-drained sandy or loamy soils, and can tolerate high temperatures and low water availability. While not currently evaluated by the IUCN, it is considered not threatened due to its wide distribution in natural and semi-urban environments.",
    'Indian Rubber Tree': "<b>Indian Rubber Tree</b>: Ficus elastica — Originally native to northeast India and Assam, the Indian Rubber Tree is now widely cultivated in South India and urban parks. It is an evergreen species prized for its ornamental value and large, glossy leaves. It prefers humid, tropical climates and grows best in moist, well-drained soil with indirect sunlight. The species is resilient in urban environments, although it is not evaluated for conservation concerns. It’s often found in gardens, botanical collections, and indoor settings.",
    'Karanj': "<b>Karanj</b>: Pongamia pinnata — Karanj, also known as Pongam, is a medium-sized tree widely distributed along riverbanks and coastal areas of Andhra Pradesh, Tamil Nadu, and Maharashtra. It plays a vital role in reforestation, oil production, and soil reclamation. It thrives in humid to semi-arid regions and adapts to saline, alkaline, and degraded soils, making it ideal for drought-prone zones. The species is not considered threatened and is promoted for use in biodiesel and agroforestry systems.",
    'Kashid': "<b>Kashid</b>: Commonly known as the Golden Shower Tree, Kashid is celebrated for its brilliant yellow flowers and is found across India except in some northern Himalayan states. It grows abundantly in Andhra Pradesh, Kerala, Assam, and Bihar. Preferring tropical dry climates, the tree grows best in full sunlight and sandy to clayey soils. It is drought-tolerant and valued in Ayurveda for its medicinal properties. The species is not evaluated, but its widespread use in landscaping keeps its population stable.",
    'Nilgiri': "<b>Nilgiri</b>: Eucalyptus species — Native to Tasmania, Eucalyptus globulus is widely cultivated in India, especially in the Nilgiris, Karnataka, and Tamil Nadu. Known for its rapid growth and essential oil production, it thrives in temperate to subtropical climates with well-drained loamy soil and moderate rainfall. Despite concerns over its water-intensive nature and allelopathic effects, it is heavily planted for commercial forestry. It is not evaluated for conservation status but monitored due to environmental impact.",
    'Pimpal': "<b>Pimpal</b>: Ficus religiosa — A sacred fig tree, Pimpal is found across India, especially near temples and village commons in Karnataka, Kerala, Assam, and central Indian states. It flourishes in humid to semi-arid regions, requiring loamy or alluvial soil and full sunlight. Known for its longevity and spiritual significance in Hinduism and Buddhism, it contributes significantly to urban ecology. The IUCN lists it as Least Concern due to its strong cultural protection and prevalence.",
    'Sita Ashok': "<b>Sita Ashok</b>: Sita Ashok is a sacred and ornamental tree found in the Western Ghats, Odisha, Assam, and Eastern Himalayas. It grows best in humid tropical climates with rich loamy soil and partial shade. Due to overharvesting for its medicinal bark and habitat loss, it is listed as Vulnerable by the IUCN. Conservation efforts are underway through plantation and in-vitro propagation techniques. It is highly regarded in Ayurveda and Indian mythology.",
    'Sonmohar': "<b>Sonmohar</b>: Delonix regia — Known for its bright yellow flowers, Sonmohar is native to Southeast Asia but widely cultivated across urban India—especially in Maharashtra, Andhra Pradesh, and Tamil Nadu. It thrives in tropical climates with moderate water and well-drained soils under full sun. Used extensively as a roadside and avenue tree, it’s fast-growing and resilient. Though not evaluated, its widespread use in cityscaping ensures its ongoing proliferation.",
    'Vad': "<b>Vad</b>: Banyan tree (Ficus benghalensis) — India’s national tree, the Banyan or Vad, is found throughout India, from Goa and Maharashtra to Assam and Himachal Pradesh. It’s famous for its vast canopy and aerial prop roots. This tree thrives in deep, well-drained soil and sunny, warm conditions, making it ideal for humid to semi-arid regions. It’s culturally revered and ecologically significant. The IUCN lists it as Not Evaluated, but it enjoys protection due to its spiritual and environmental importance.",
    'Vilayati Chinch': "<b>Vilayati Chinch</b>: Native to Mexico and Central America, Vilayati Chinch has been widely naturalized across India, especially in Telangana, Tamil Nadu, and Maharashtra. It tolerates dry, arid climates and thrives in poor, rocky soils, requiring minimal water and full sun. Known for its coiled pods and tangy-sweet pulp, the tree is drought-resistant and useful in roadside plantations. It is considered Least Concern due to its wide adaptability and hardiness."
}

plant_geo = {
    'Apta': {
        'desc': disease_dic['Apta'],
        'scientific_name': 'Bauhinia racemosa',
        'flowering_season': 'August to November',
        'uses': 'Used in Ayurveda for treating asthma, wounds, and diarrhea.',
        'biodiversity_zone': 'Western Ghats (Semi-Evergreen Forests)',
        'locations': [
            {'lat': 18.5100, 'lng': 73.8567, 'place': 'Vetal Tekdi, Pune, Maharashtra'},
            {'lat': 19.8762, 'lng': 75.3433, 'place': 'Daulatabad Fort, Aurangabad, Maharashtra'}
        ],
        'census': {
            'estimated_count': 120000,
            'status': 'Least Concern',
            'year': 2023
        }
    },
    'Indian Rubber Tree': {
        'desc': disease_dic['Indian Rubber Tree'],
        'scientific_name': 'Ficus elastica',
        'flowering_season': 'Rarely flowers; mainly propagated by cuttings',
        'uses': 'Ornamental and indoor plant; air purification.',
        'biodiversity_zone': 'Tropical Wet Evergreen Forests',
        'locations': [
            {'lat': 11.0168, 'lng': 76.9558, 'place': 'VOC Park, Coimbatore, Tamil Nadu'},
            {'lat': 10.8505, 'lng': 76.2711, 'place': 'Silent Valley, Palakkad, Kerala'}
        ],
        'census': {
            'estimated_count': 300000,
            'status': 'Common',
            'year': 2022
        }
    },
    'Karanj': {
        'desc': disease_dic['Karanj'],
        'scientific_name': 'Pongamia pinnata',
        'flowering_season': 'March to June',
        'uses': 'Biodiesel, traditional medicine, shade tree.',
        'biodiversity_zone': 'Deccan Plateau Dry Deciduous Forests',
        'locations': [
            {'lat': 17.3850, 'lng': 78.4867, 'place': 'KBR Park, Hyderabad, Telangana'},
            {'lat': 15.3173, 'lng': 75.7139, 'place': 'Unkal Lake, Hubli, Karnataka'}
        ],
        'census': {
            'estimated_count': 80000,
            'status': 'Vulnerable',
            'year': 2021
        }
    },
    'Kashid': {
        'desc': disease_dic['Kashid'],
        'scientific_name': 'Casuarina equisetifolia',
        'flowering_season': 'Throughout the year',
        'uses': 'Coastal protection, timber, fuelwood.',
        'biodiversity_zone': 'Littoral and Swamp Forests',
        'locations': [
            {'lat': 18.4370, 'lng': 72.8786, 'place': 'Kashid Beach, Raigad, Maharashtra'},
            {'lat': 18.2502, 'lng': 73.1636, 'place': 'Murud Beach Forest, Maharashtra'}
        ],
        'census': {
            'estimated_count': 45000,
            'status': 'Near Threatened',
            'year': 2020
        }
    },
    'Nilgiri': {
        'desc': disease_dic['Nilgiri'],
        'scientific_name': 'Eucalyptus globulus',
        'flowering_season': 'December to March',
        'uses': 'Essential oils, anti-inflammatory, antimicrobial.',
        'biodiversity_zone': 'Montane Forests of Western Ghats',
        'locations': [
            {'lat': 11.4064, 'lng': 76.6932, 'place': 'Botanical Gardens, Ooty, Tamil Nadu'},
            {'lat': 11.6512, 'lng': 76.2590, 'place': 'Needle Rock, Gudalur, Tamil Nadu'}
        ],
        'census': {
            'estimated_count': 150000,
            'status': 'Least Concern',
            'year': 2023
        }
    },
    'Pimpal': {
        'desc': disease_dic['Pimpal'],
        'scientific_name': 'Ficus religiosa',
        'flowering_season': 'April to June',
        'uses': 'Worship, air purification, Ayurveda.',
        'biodiversity_zone': 'Central Indian Mixed Forests',
        'locations': [
            {'lat': 23.1793, 'lng': 75.7849, 'place': 'Pipaldhara, Ujjain, Madhya Pradesh'},
            {'lat': 19.9975, 'lng': 73.7898, 'place': 'Gangapur Forest, Nashik, Maharashtra'}
        ],
        'census': {
            'estimated_count': 200000,
            'status': 'Common',
            'year': 2022
        }
    },
    'Sita Ashok': {
        'desc': disease_dic['Sita Ashok'],
        'scientific_name': 'Saraca asoca',
        'flowering_season': 'February to April',
        'uses': 'Traditional medicine (Ashokarishta), rituals.',
        'biodiversity_zone': 'Moist Deciduous Forests of Eastern Ghats',
        'locations': [
            {'lat': 20.2703, 'lng': 85.8339, 'place': 'Nandankanan Garden, Bhubaneswar, Odisha'},
            {'lat': 21.2554, 'lng': 81.6331, 'place': 'Raipur Urban Forest, Chhattisgarh'}
        ],
        'census': {
            'estimated_count': 65000,
            'status': 'Rare',
            'year': 2023
        }
    },
    'Sonmohar': {
        'desc': disease_dic['Sonmohar'],
        'scientific_name': 'Delonix regia',
        'flowering_season': 'April to June',
        'uses': 'Ornamental, shade tree.',
        'biodiversity_zone': 'Urban Agroforestry Zones',
        'locations': [
            {'lat': 18.5089, 'lng': 73.8077, 'place': 'Taljai Hill, Pune, Maharashtra'},
            {'lat': 19.8762, 'lng': 75.3433, 'place': 'Aurangabad City Parks, Maharashtra'}
        ],
        'census': {
            'estimated_count': 57000,
            'status': 'Least Concern',
            'year': 2021
        }
    },
    'Vad': {
        'desc': disease_dic['Vad'],
        'scientific_name': 'Ficus benghalensis',
        'flowering_season': 'March to May',
        'uses': 'Cultural importance, shade, air purifier.',
        'biodiversity_zone': 'Central Indian Mixed Deciduous Forests',
        'locations': [
            {'lat': 22.3072, 'lng': 73.1812, 'place': 'Vadodara Banyan Reserve, Gujarat'},
            {'lat': 21.1458, 'lng': 79.0882, 'place': 'Sitabuldi Fort, Nagpur, Maharashtra'}
        ],
        'census': {
            'estimated_count': 180000,
            'status': 'Common',
            'year': 2023
        }
    },
    'Vilayati Chinch': {
        'desc': disease_dic['Vilayati Chinch'],
        'scientific_name': 'Prosopis juliflora',
        'flowering_season': 'March to May',
        'uses': 'Fuelwood, erosion control, invasive',
        'biodiversity_zone': 'Dry Arid Scrublands',
        'locations': [
            {'lat': 17.1232, 'lng': 79.2089, 'place': 'Warangal Plateau, Telangana'},
            {'lat': 16.5062, 'lng': 80.6480, 'place': 'Vijayawada Outskirts, Andhra Pradesh'}
        ],
        'census': {
            'estimated_count': 70000,
            'status': 'Invasive Species',
            'year': 2022
        }
    }
}

