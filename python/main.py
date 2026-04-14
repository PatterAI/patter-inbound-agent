"""Minimal inbound voice agent — answer phone calls with AI."""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from patter import Patter

phone = Patter(
    mode="local",
    openai_key=os.getenv("OPENAI_API_KEY"),
    twilio_sid=os.getenv("TWILIO_ACCOUNT_SID"),
    twilio_token=os.getenv("TWILIO_AUTH_TOKEN"),
    phone_number=os.getenv("TWILIO_PHONE_NUMBER"),
    webhook_url=os.getenv("WEBHOOK_URL"),
)

agent = phone.agent(
    system_prompt=(
        "You are a friendly reservation assistant for La Dolce Vita, "
        "an Italian restaurant in downtown San Francisco. Help callers "
        "make, modify, or cancel reservations. Ask for the date, time, "
        "party size, and a name for the reservation. Be warm and concise."
    ),
    voice="nova",
    first_message=(
        "Thanks for calling La Dolce Vita! "
        "How can I help you with a reservation today?"
    ),
)

if __name__ == "__main__":
    asyncio.run(phone.serve(agent, port=8000))
