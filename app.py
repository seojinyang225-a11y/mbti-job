import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천기",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 MBTI 진로 추천기")
st.write("나의 MBTI를 선택하면 잘 어울리는 진로를 추천해줄게! 😎")

# MBTI 데이터
career_data = {
    "INTJ": [
        {
            "job": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 통계학과",
            "personality": "논리적이고 분석하는 걸 좋아하는 사람에게 찰떡!"
        },
        {
            "job": "🚀 연구원",
            "major": "물리학과, 화학과",
            "personality": "혼자 깊게 탐구하고 새로운 아이디어를 좋아하는 성격!"
        }
    ],
    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 문제 해결을 즐기는 사람에게 추천!"
        },
        {
            "job": "🔬 과학자",
            "major": "생명과학과, 물리학과",
            "personality": "끊임없이 질문하고 탐구하는 성격과 잘 맞아!"
        }
    ],
    "ENTJ": [
        {
            "job": "📈 CEO",
            "major": "경영학과, 경제학과",
            "personality": "리더십 강하고 목표 지향적인 사람에게 딱!"
        },
        {
            "job": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적으로 말하고 설득 잘하는 성격에게 추천!"
        }
    ],
    "ENTP": [
        {
            "job": "🎤 마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "아이디어 넘치고 사람 만나는 걸 좋아하는 타입!"
        },
        {
            "job": "📺 콘텐츠 크리에이터",
            "major": "미디어학과, 영상학과",
            "personality": "창의력 폭발🔥 재미있는 걸 좋아하는 사람에게 추천!"
        }
    ],
    "INFJ": [
        {
            "job": "💖 상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 사람 마음을 잘 이해해!"
        },
        {
            "job": "📚 작가",
            "major": "문예창작과",
            "personality": "상상력이 풍부하고 감수성이 깊은 성격!"
        }
    ],
    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과, 미술학과",
            "personality": "감성적이고 창의적인 사람에게 추천!"
        },
        {
            "job": "🎵 음악가",
            "major": "실용음악과",
            "personality": "자기만의 감정을 표현하는 걸 좋아하는 타입!"
        }
    ],
    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람을 이끌고 도와주는 걸 좋아하는 성격!"
        },
        {
            "job": "🤝 HR 담당자",
            "major": "경영학과, 심리학과",
            "personality": "사람들과 잘 어울리고 배려심 많은 타입!"
        }
    ],
    "ENFP": [
        {
            "job": "✈️ 여행 기획자",
            "major": "관광학과",
            "personality": "활발하고 새로운 경험을 좋아하는 사람!"
        },
        {
            "job": "🎬 방송인",
            "major": "방송연예과",
            "personality": "에너지 넘치고 분위기 메이커인 성격!"
        }
    ],
    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 강한 사람에게 추천!"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 성격!"
        }
    ],
    "ISFJ": [
        {
            "job": "🩺 간호사",
            "major": "간호학과",
            "personality": "따뜻하고 남을 잘 챙기는 타입!"
        },
        {
            "job": "🏫 사회복지사",
            "major": "사회복지학과",
            "personality": "배려심 많고 책임감 있는 성격!"
        }
    ],
    "ESTJ": [
        {
            "job": "📊 공무원",
            "major": "행정학과",
            "personality": "체계적이고 리더십 있는 사람!"
        },
        {
            "job": "🏢 관리자",
            "major": "경영학과",
            "personality": "계획 세우고 관리하는 걸 잘하는 타입!"
        }
    ],
    "ESFJ": [
        {
            "job": "🎉 이벤트 플래너",
            "major": "호텔관광학과",
            "personality": "사람들과 함께하는 걸 좋아하는 성격!"
        },
        {
            "job": "👩‍⚕️ 보건교사",
            "major": "간호학과, 교육학과",
            "personality": "친절하고 세심한 사람에게 추천!"
        }
    ],
    "ISTP": [
        {
            "job": "🔧 엔지니어",
            "major": "기계공학과",
            "personality": "직접 만들고 해결하는 걸 좋아하는 타입!"
        },
        {
            "job": "🛩️ 파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 상황 판단 빠른 사람!"
        }
    ],
    "ISFP": [
        {
            "job": "📸 사진작가",
            "major": "사진학과",
            "personality": "감각적이고 자유로운 성격!"
        },
        {
            "job": "💄 메이크업 아티스트",
            "major": "뷰티학과",
            "personality": "섬세하고 예술 감각 있는 사람!"
        }
    ],
    "ESTP": [
        {
            "job": "🏅 스포츠 코치",
            "major": "체육학과",
            "personality": "활동적이고 도전 좋아하는 성격!"
        },
        {
            "job": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "말 잘하고 에너지 넘치는 타입!"
        }
    ],
    "ESFP": [
        {
            "job": "🎤 연예인",
            "major": "연극영화과",
            "personality": "사람들 앞에서 빛나는 걸 좋아하는 성격!"
        },
        {
            "job": "🍰 파티시에",
            "major": "제과제빵학과",
            "personality": "감각적이고 즐거움을 주는 걸 좋아하는 타입!"
        }
    ]
}

# MBTI 선택
mbti = st.selectbox(
    "👇 너의 MBTI를 골라봐!",
    list(career_data.keys())
)

# 결과 출력
if mbti:
    st.subheader(f"✨ {mbti} 유형에게 추천하는 진로!")

    for career in career_data[mbti]:
        st.markdown(f"""
        ---
        ### {career['job']}

        🎓 **추천 학과**
        - {career['major']}

        🌈 **잘 맞는 성격**
        - {career['personality']}
        """)

    st.success("😆 진로 추천 결과가 나왔어! 참고해서 미래를 멋지게 준비해봐 🚀")
