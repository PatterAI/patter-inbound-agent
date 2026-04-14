/**
 * Minimal inbound voice agent — answer phone calls with AI.
 *
 * Usage: npx tsx main.ts
 */

import { Patter } from "getpatter";
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const phone = new Patter({
  mode: "local",
  openaiKey: process.env.OPENAI_API_KEY!,
  twilioSid: process.env.TWILIO_ACCOUNT_SID!,
  twilioToken: process.env.TWILIO_AUTH_TOKEN!,
  phoneNumber: process.env.TWILIO_PHONE_NUMBER!,
  webhookUrl: process.env.WEBHOOK_URL!,
});

const agent = phone.agent({
  systemPrompt: `You are a friendly reservation assistant for "La Cucina Bella",
an Italian restaurant. Help callers book tables, answer questions about the menu,
and provide directions. Be warm, concise, and professional.`,
  voice: "nova",
  firstMessage:
    "Hello! Thank you for calling La Cucina Bella. How can I help you today?",
});

async function main(): Promise<void> {
  await phone.serve({ agent, port: 8000 });
}

main();
