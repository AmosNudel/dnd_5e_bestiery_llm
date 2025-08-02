from agents import Agent, Runner, handoff
from dotenv import load_dotenv
import os
import asyncio
from bestiary_tools import *
from spellcasting_tools import *

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set")



bestiary_tools = [
    read_bestiary_by_name,
    read_bestiary_by_cr,
    read_bestiary_by_type,
    read_bestiary_by_size,
    read_bestiary_by_environment,
    read_monster_fluff
]

spellcasting_tools = [
    read_spell_by_name,
    read_spell_by_school,
    read_spell_by_level
]

bestiary_agent = Agent(
    name="Bestiary Agent",
    instructions=("You are a helpful assistant that can search the bestiary for creatures and answer questions about them."
                  "If the creature has fluff call the read_monster_fluff tool to get the fluff."
                  "If the query has a spellnig or grammer mistake, correct it on your own."),
    tools=bestiary_tools,
    model="gpt-4o-mini",
)

spellcasting_agent = Agent(
    name="Spellcasting Agent",
    instructions=("You are a helpful assistant that can search the spellcasting tools for spells and answer questions about them."
                  "If the query has a spellnig or grammer mistake, correct it on your own."),
    tools=spellcasting_tools,
    model="gpt-4o-mini",
)

router_agent = Agent(
    name="Router Agent",
    instructions=("You are a helpful assistant that can route questions to the bestiary or spellcasting agent."
                  "If the query is about a creature, route it to the bestiary agent."
                  "If the query is about a spell, route it to the spellcasting agent."
                  "ALWAYS start your response by telling the user which agent you are routing the question to."
                  "For example: 'I'm routing this to the Bestiary Agent because you're asking about creatures.'"),
    handoffs=[bestiary_agent, spellcasting_agent],
)

async def main():
    # bestiary_result = await Runner.run(bestiary_agent, "what can you tell me about adult white dragons?")
    # print(bestiary_result.final_output)

    # spellcasting_result = await Runner.run(spellcasting_agent, "give me a complete list of all cantrips?")
    # print(spellcasting_result.final_output)

    router_result = await Runner.run(router_agent, "what kind of sphinxes are there?")
    print(router_result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

