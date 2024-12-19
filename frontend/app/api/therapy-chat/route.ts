import { NextResponse } from 'next/server';
import axios from 'axios';

interface ChatResponse {
  text: string;
  audio?: string;
}

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    const message = formData.get('message');
    const clientId = formData.get('clientId'); // Assuming you need clientId

    if (!message || typeof message !== 'string') {
      return NextResponse.json(
        { error: "Valid message is required" },
        { status: 400 }
      );
    }

    if (!clientId || typeof clientId !== 'string') {
      return NextResponse.json(
        { error: "Valid clientId is required" },
        { status: 400 }
      );
    }

    const response = await axios.post<ChatResponse>(
      'https://therapist-chatbot-1.onrender.com/message', // Corrected endpoint
      {
        client_id: clientId, // Ensure backend expects 'client_id'
        message: message.trim(),
      },
      {
        headers: {
          'Content-Type': 'application/json',
        }
      }
    );

    if (!response.data.text) {
      throw new Error('Invalid response from AI service');
    }

    return NextResponse.json({
      text: response.data.text,
      audio: response.data.audio
    });

  } catch (error) {
    console.error('Error:', error);
    return NextResponse.json(
      { error: "AI service unavailable" },
      { status: 500 }
    );
  }
}
