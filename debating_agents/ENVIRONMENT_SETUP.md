# Environment Setup for CrewAI Debating Agents

This guide shows you how to set up environment variables for your CrewAI project.

## Quick Setup

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file with your actual API keys:**
   ```bash
   # Replace with your actual OpenAI API key
   OPENAI_API_KEY=sk-your-actual-openai-api-key-here
   
   # Optional: Anthropic API key for Claude models
   ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-api-key-here
   ```

3. **Run your crew:**
   ```bash
   crewai run
   # or
   python3 src/debating_agents/main.py
   ```

## Environment Variables

### Required Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required for most operations)

### Optional Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key (for Claude models)
- `DEFAULT_MOTION`: Default debate motion (default: "Is spending for college tuition a good investment?")
- `MAX_DEBATE_ROUNDS`: Maximum number of debate rounds (default: 1)
- `DEBUG`: Enable debug mode (default: false)
- `LOG_LEVEL`: Logging level (default: info)

### Custom Configuration

You can also use environment variables in your agent configuration files:

```yaml
# In agents.yaml
judge:
  role: >
    Decide the winner of the debate
  llm: ${DEBATE_LLM_MODEL:-openai/gpt-4o-mini}  # Uses env var or defaults to gpt-4o-mini
```

## How It Works

The project automatically loads environment variables from the `.env` file in the project root. The `main.py` file includes:

1. **Automatic .env loading**: Uses `python-dotenv` to load variables
2. **API key validation**: Checks if your API keys are properly configured
3. **Environment-based configuration**: Uses env vars for customizable settings
4. **Helpful error messages**: Shows troubleshooting tips when things go wrong

## Security Notes

- The `.env` file is already in `.gitignore` to prevent committing API keys
- Never commit your actual API keys to version control
- Use `.env.example` as a template for others

## Troubleshooting

If you see "API key not properly configured":
1. Make sure your `.env` file exists in the project root
2. Check that your API key doesn't start with "your_" (placeholder text)
3. Verify your API key is correct and has sufficient credits
4. Ensure your internet connection is working

## Example .env File

```bash
# OpenAI API Key (required)
OPENAI_API_KEY=sk-proj-abc123...

# Anthropic API Key (optional)
ANTHROPIC_API_KEY=sk-ant-abc123...

# Custom debate settings
DEFAULT_MOTION="Is artificial intelligence beneficial for society?"
MAX_DEBATE_ROUNDS=3

# Debug settings
DEBUG=false
LOG_LEVEL=info
```
