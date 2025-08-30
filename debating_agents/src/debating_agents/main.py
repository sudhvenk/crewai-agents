#!/usr/bin/env python
import sys
import warnings
import os
from pathlib import Path
from dotenv import load_dotenv

from datetime import datetime

from debating_agents.crew import DebatingAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Load environment variables from .env file
def load_environment():
    """Load environment variables from .env file"""
    # Get the project root directory (where .env file is located)
    project_root = Path(__file__).parent.parent.parent
    env_path = project_root / '.env'
    
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ Loaded environment variables from {env_path}")
        
        # Check if required API keys are set
        openai_key = os.getenv('OPENAI_API_KEY')
        if openai_key and not openai_key.startswith('your_'):
            print("✅ OpenAI API key is configured")
        else:
            print("⚠️  OpenAI API key not properly configured")
            print("   Please set OPENAI_API_KEY in your .env file")

        gemini_key = os.getenv('GEMINI_API_KEY')
        if gemini_key and not gemini_key.startswith('your_'):   
            print("✅ GEMINI_API_KEY is configured")
        else:
            print("⚠️  GEMINI_API_KEY not properly configured")
            print("   Please set GEMINI_API_KEY in your .env file") 

        anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        if anthropic_key and not anthropic_key.startswith('your_'):
            print("✅ Anthropic API key is configured")
        else:
            print("⚠️  Anthropic API key not properly configured")
            print("   Please set ANTHROPIC_API_KEY in your .env file")  
            
    else:
        print(f"⚠️  No .env file found at {env_path}")
        print("   You can create one with your API keys and other configuration")
        print("   Copy .env.example to .env and fill in your actual API keys")

def get_debate_inputs():
    """Get debate inputs from environment variables or use defaults"""
    # Get motion from environment variable or use default
    motion = os.getenv('DEFAULT_MOTION', 'Is spending for college tuition a good investment?')
    
    # Get max rounds from environment variable
    max_rounds = int(os.getenv('MAX_DEBATE_ROUNDS', '1'))
    
    return {
        'motion': motion,
        'max_rounds': max_rounds
    }

def run_single_round(round_number, motion, previous_context=""):
    """Run a single round of debate"""
    print(f"\n{'='*60}")
    print(f"🥊 ROUND {round_number}")
    print(f"{'='*60}")
    
    inputs = {
        'motion': motion,
        'round_number': round_number,
        'previous_context': previous_context
    }
    
    try:
        result = DebatingAgents().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        print(f"❌ Error in round {round_number}: {e}")
        return None

def run():
    """
    Run the crew with multiple rounds if configured.
    """
    # Load environment variables first
    load_environment()
    
    # Get inputs from environment or use defaults
    inputs = get_debate_inputs()
    
    print(f"🎯 Debate Motion: {inputs['motion']}")
    print(f"🔄 Max Rounds: {inputs['max_rounds']}")
    print()
    
    if inputs['max_rounds'] == 1:
        # Single round - use original behavior
        try:
            result = DebatingAgents().crew().kickoff(inputs=inputs)
            print("\n" + "="*80)
            print("🏆 FINAL RESULT:")
            print("="*80)
            print(result)
        except Exception as e:
            print(f"\n❌ Error occurred while running the crew: {e}")
            print("\n💡 Troubleshooting tips:")
            print("   1. Make sure your .env file exists and contains valid API keys")
            print("   2. Check that your API keys are correct and have sufficient credits")
            print("   3. Verify your internet connection")
            raise Exception(f"An error occurred while running the crew: {e}")
    
    else:
        # Multiple rounds
        print(f"🚀 Starting {inputs['max_rounds']} rounds of debate...")
        
        all_results = []
        previous_context = ""
        
        for round_num in range(1, inputs['max_rounds'] + 1):
            result = run_single_round(round_num, inputs['motion'], previous_context)
            
            if result:
                all_results.append(f"Round {round_num}: {result}")
                # Build context for next round
                previous_context += f"Round {round_num} result: {result}\n"
            else:
                print(f"❌ Round {round_num} failed, stopping debate")
                break
        
        # Final summary
        print(f"\n{'='*80}")
        print("🏆 DEBATE SUMMARY")
        print(f"{'='*80}")
        print(f"Motion: {inputs['motion']}")
        print(f"Total Rounds: {len(all_results)}")
        print()
        
        for i, result in enumerate(all_results, 1):
            print(f"Round {i}:")
            print("-" * 40)
            print(result)
            print()

if __name__ == "__main__":
    run()
