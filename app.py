import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 & 포켓몬 추천기",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 MBTI 진로 & 포켓몬 추천기")
st.write("MBTI를 선택하면 ✨ 어울리는 진로와 🐾 닮은 포켓몬까지 추천해줄게!")

# ---------------------------
# MBTI 데이터
# ---------------------------

mbti_data = {
    "INTJ": {
        "pokemon": {
            "name": "뮤츠",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
            "personality": "🧠 전략적이고 똑똑한 완벽주의자! 혼자 깊게 생각하는 걸 좋아해."
        },
        "careers": [
            {
                "job": "🧠 데이터 사이언티스트",
                "major": "컴퓨터공학과, 통계학과",
                "personality": "논리적이고 분석하는 걸 좋아하는 사람!"
            },
            {
                "job": "🚀 연구원",
                "major": "물리학과, 화학과",
                "personality": "탐구심이 강하고 새로운 아이디어를 좋아하는 타입!"
            }
        ]
    },

    "INTP": {
        "pokemon": {
            "name": "후딘",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
            "personality": "💡 호기심 천재! 생각하는 걸 좋아하고 아이디어가 넘쳐!"
        },
        "careers": [
            {
                "job": "💻 프로그래머",
                "major": "소프트웨어학과, 컴퓨터공학과",
                "personality": "문제 해결을 좋아하는 성격!"
            },
            {
                "job": "🔬 과학자",
                "major": "생명과학과, 물리학과",
                "personality": "끊임없이 질문하고 탐구하는 타입!"
            }
        ]
    },

    "ENTJ": {
        "pokemon": {
            "name": "리자몽",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
            "personality": "🔥 카리스마 넘치는 리더! 목표를 향해 돌진하는 스타일!"
        },
        "careers": [
            {
                "job": "📈 CEO",
                "major": "경영학과, 경제학과",
                "personality": "리더십 강하고 추진력 있는 사람!"
            },
            {
                "job": "⚖️ 변호사",
                "major": "법학과",
                "personality": "논리적이고 설득 잘하는 타입!"
            }
        ]
    },

    "ENTP": {
        "pokemon": {
            "name": "팬텀",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
            "personality": "😎 장난기 많고 창의력 폭발! 새로운 걸 좋아해."
        },
        "careers": [
            {
                "job": "🎤 마케팅 기획자",
                "major": "광고홍보학과",
                "personality": "아이디어 넘치고 사람 만나는 걸 좋아해!"
            },
            {
                "job": "📺 콘텐츠 크리에이터",
                "major": "영상학과, 미디어학과",
                "personality": "창의적인 활동을 즐기는 타입!"
            }
        ]
    },

    "INFJ": {
        "pokemon": {
            "name": "루기아",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
            "personality": "🌊 조용하지만 깊은 카리스마! 공감 능력이 뛰어나!"
        },
        "careers": [
            {
                "job": "💖 상담사",
                "major": "심리학과",
                "personality": "사람 마음을 잘 이해하는 타입!"
            },
            {
                "job": "📚 작가",
                "major": "문예창작과",
                "personality": "감수성이 풍부하고 상상력이 뛰어나!"
            }
        ]
    },

    "INFP": {
        "pokemon": {
            "name": "이브이",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
            "personality": "🌸 따뜻하고 감성적인 몽상가! 자기만의 세계가 있어."
        },
        "careers": [
            {
                "job": "🎨 일러스트레이터",
                "major": "디자인학과, 미술학과",
                "personality": "창의적이고 감성적인 사람!"
            },
            {
                "job": "🎵 음악가",
                "major": "실용음악과",
                "personality": "감정을 표현하는 걸 좋아하는 타입!"
            }
        ]
    },

    "ENFJ": {
        "pokemon": {
            "name": "피카츄",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "personality": "⚡ 모두와 잘 어울리는 인기쟁이! 따뜻한 리더 스타일!"
        },
        "careers": [
            {
                "job": "👩‍🏫 교사",
                "major": "교육학과",
                "personality": "사람을 도와주는 걸 좋아해!"
            },
            {
                "job": "🤝 HR 담당자",
                "major": "경영학과, 심리학과",
                "personality": "배려심 많고 친화력 좋은 타입!"
            }
        ]
    },

    "ENFP": {
        "pokemon": {
            "name": "토게피",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
            "personality": "✨ 밝고 에너지 넘치는 분위기 메이커!"
        },
        "careers": [
            {
                "job": "✈️ 여행 기획자",
                "major": "관광학과",
                "personality": "새로운 경험을 좋아하는 성격!"
            },
            {
                "job": "🎬 방송인",
                "major": "방송연예과",
                "personality": "에너지 넘치고 활발한 타입!"
            }
        ]
    },

    "ISTJ": {
        "pokemon": {
            "name": "거북왕",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
            "personality": "🛡️ 책임감 강하고 믿음직한 현실주의자!"
        },
        "careers": [
            {
                "job": "🏦 회계사",
                "major": "회계학과",
                "personality": "꼼꼼하고 계획적인 사람!"
            },
            {
                "job": "👮 경찰관",
                "major": "경찰행정학과",
                "personality": "원칙을 중요하게 생각하는 타입!"
            }
        ]
    },

    "ISFP": {
        "pokemon": {
            "name": "나인테일",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png",
            "personality": "🎨 감성적이고 자유로운 예술가 스타일!"
        },
        "careers": [
            {
                "job": "📸 사진작가",
                "major": "사진학과",
                "personality": "감각적이고 섬세한 사람!"
            },
            {
                "job": "💄 메이크업 아티스트",
                "major": "뷰티학과",
                "personality": "예술 감각 뛰어난 타입!"
            }
        ]
    },

    "ESTP": {
        "pokemon": {
            "name": "괴력몬",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
            "personality": "💪 도전 정신 MAX! 행동력이 엄청난 타입!"
        },
        "careers": [
            {
                "job": "🏅 스포츠 코치",
                "major": "체육학과",
                "personality": "활동적이고 에너지 넘치는 사람!"
            },
            {
                "job": "💼 영업 전문가",
                "major": "경영학과",
                "personality": "말 잘하고 자신감 있는 타입!"
            }
        ]
    },

    "ESFP": {
        "pokemon": {
            "name": "푸린",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
            "personality": "🎤 사람들의 관심을 받는 걸 좋아하는 핵인싸!"
        },
        "careers": [
            {
                "job": "🎬 연예인",
                "major": "연극영화과",
                "personality": "사람들 앞에서 빛나는 걸 좋아해!"
            },
            {
                "job": "🍰 파티시에",
                "major": "제과제빵학과",
                "personality": "감각적이고 즐거움을 주는 타입!"
            }
        ]
    }
}

# 부족한 MBTI 자동 추가용
all_mbti = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

# 없는 MBTI는 기본값 추가
for mbti in all_mbti:
    if mbti not in mbti_data:
        mbti_data[mbti] = {
            "pokemon": {
                "name": "메타몽",
                "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
                "personality": "🌟 다양한 매력을 가진 특별한 성격!"
            },
            "careers": [
                {
                    "job": "💼 다양한 직업 가능!",
                    "major": "여러 학과",
                    "personality": "자신의 장점을 잘 살리면 무엇이든 가능!"
                },
                {
                    "job": "🚀 미래의 멋진 인재",
                    "major": "관심 있는 분야",
                    "personality": "도전하면서 성장하는 타입!"
                }
            ]
        }

# ---------------------------
# 선택 UI
# ---------------------------

selected_mbti = st.selectbox(
    "👇 너의 MBTI를 선택해봐!",
    all_mbti
)

data = mbti_data[selected_mbti]

# ---------------------------
# 포켓몬 추천
# ---------------------------

st.markdown("---")
st.header("🐾 너와 닮은 포켓몬!")

st.image(data["pokemon"]["image"], width=180)

st.subheader(f"✨ {data['pokemon']['name']}")

st.write(data["pokemon"]["personality"])

# ---------------------------
# 진로 추천
# ---------------------------

st.markdown("---")
st.header("🎓 추천 진로")

for career in data["careers"]:
    st.markdown(f"""
    ### {career['job']}

    🎓 **추천 학과**
    - {career['major']}

    🌈 **어울리는 성격**
    - {career['personality']}

    ---
    """)

st.success("😆 결과가 완성됐어! 너의 장점을 살려 멋진 미래를 만들어봐 🚀✨")
