#from fastapi import APIRouter, Header, HTTPException, Depends
from models_1 import UserInput, ChatResponse
import os
from fastapi import APIRouter, Header, HTTPException, Depends
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
API_KEY = os.getenv("API_KEY")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

def chatbot_response(message):
    msg = message.lower()

    # 🚨 Crisis / Suicide
    if any(word in msg for word in ['suicidal', 'kill myself', 'end it all', 'want to die', 'no reason to live', 'take my life', 'can’t go on']):
        return (
            "You're not alone, and your life matters. Please seek help immediately — professionals and loved ones care deeply for you.",
            "high",
            ["Call 911", "Crisis Text Line (Text HOME to 741741)", "National Suicide Prevention Lifeline: 1-800-273-TALK"]
        )

    # 😞 Depression / Sadness
    elif any(word in msg for word in ['depressed', 'hopeless', 'worthless', 'sad', 'down', 'empty', 'nothing matters']):
        return (
            "It sounds like you're really struggling. Reaching out is a strong step. You deserve support and healing.",
            "medium",
            ["BetterHelp", "National Helpline: 1-800-662-HELP", "TherapyForBlackGirls.com"]
        )

    # 😰 Anxiety / Panic
    elif any(word in msg for word in ['anxious', 'panic', 'nervous', 'scared', 'can’t breathe', 'overwhelmed']):
        return (
            "Anxiety can be overwhelming, but you're not alone. Try grounding techniques or slow breathing.",
            "medium",
            ["Headspace (Anxiety Section)", "Calm App", "Mindfulness Guide"]
        )

    # 😡 Anger / Rage
    elif any(word in msg for word in ['angry', 'rage', 'furious', 'irritated', 'can’t control']):
        return (
            "Anger is a valid emotion. Taking a moment to pause, breathe, or vent constructively can help ease it.",
            "medium",
            ["Anger Management Tips", "MoodTools", "Healthy Coping Skills"]
        )

    # 😔 Loneliness / Isolation
    elif any(word in msg for word in ['lonely', 'alone', 'isolated', 'no one cares', 'abandoned']):
        return (
            "Loneliness can feel crushing. But you are seen, and there are people and communities who care deeply.",
            "medium",
            ["7 Cups", "ReachOut Forums", "Supportive Friends app"]
        )

    # 💤 Exhaustion / Burnout
    elif any(word in msg for word in ['burnt out', 'exhausted', 'tired of everything', 'drained', 'can’t function']):
        return (
            "You might be emotionally or physically drained. Rest is not a weakness — it’s vital to your well-being.",
            "medium",
            ["Take a break guide", "Meditation Apps", "Mental Health America Burnout Toolkit"]
        )

    # 😨 Trauma / Fear
    elif any(word in msg for word in ['trauma', 'abused', 'assault', 'afraid', 'terrified']):
        return (
            "You're incredibly brave for opening up. Please consider speaking to a trauma-informed professional.",
            "high",
            ["RAINN.org", "1in6.org (for men)", "Safe Horizon"]
        )

    # 😭 Grief / Loss
    elif any(word in msg for word in ['lost someone', 'grief', 'mourning', 'death in family', 'can’t move on']):
        return (
            "Loss is so deeply painful. Be gentle with yourself — grieving is not linear, and you don’t have to go through it alone.",
            "medium",
            ["GriefShare.org", "The Dinner Party", "Modern Loss"]
        )

    # 😌 Hope / Healing
    elif any(word in msg for word in ['healing', 'recovering', 'doing better', 'hopeful']):
        return (
            "That’s wonderful to hear. Keep nurturing your journey — healing takes courage and time.",
            "low",
            ["Self-care checklist", "Positive Psychology Toolkit"]
        )

    # ❤️ Gratitude / Positivity
    elif any(word in msg for word in ['grateful', 'thankful', 'happy', 'joyful', 'optimistic']):
        return (
            "That’s beautiful to hear! Keep shining — your joy is powerful and can inspire others too.",
            "low",
            ["Gratitude journaling prompts", "Happier App", "Tiny Buddha blog"]
        )

    # ❓ Confusion / Disorientation
    elif any(word in msg for word in ['confused', 'don’t know', 'can’t decide', 'mixed feelings']):
        return (
            "Feeling uncertain is okay. Sometimes talking things through or journaling can bring clarity.",
            "low",
            ["Mental Clarity Guide", "Decision-Making Tools", "Support groups on Reddit (like r/DecidingToBeBetter)"]
        )

    # 🌿 Default supportive fallback
    else:
        return (
            "Thank you for sharing. Whatever you're feeling, you're not alone. I'm here to support you — feel free to open up more.",
            "low",
            []
        )

@router.post("/analyze", response_model=ChatResponse, dependencies=[Depends(verify_api_key)])
def analyze_message(input: UserInput):
    response_msg, severity, resources = chatbot_response(input.message)
    return ChatResponse(
        message=response_msg,
        severity=severity,
        suggested_resources=resources
    )
