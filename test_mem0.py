from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json

# Load environment variables
load_dotenv()

# User name
user_name = "Mahesh"

# Initialize Mem0 client
mem0 = MemoryClient()


def add_memory():
    messages_formatted = [
        {
            "role": "user",
            "content": "I really like Linkin Park."
        },
        {
            "role": "assistant",
            "content": "That is a good choice."
        },
        {
            "role": "user",
            "content": "I think so too."
        },
        {
            "role": "assistant",
            "content": "What is your favorite song by them?"
        },
    ]

    # Add memory
    mem0.add(messages_formatted, user_id="Mahesh")
    print("✅ Memory added successfully!\n")


def get_memory_by_query():
    query = f"What are {user_name}'s preferences?"

    # Correct search usage
    results = mem0.search(
        query,
        filters={"user_id": user_name}
    )

    memories = []

    for result in results:
        # Handle both dict and string responses
        if isinstance(result, dict):
            memories.append({
                "memory": result.get("memory"),
                "updated_at": result.get("updated_at")
            })
        else:
            memories.append({
                "memory": result,
                "updated_at": None
            })

    memories_str = json.dumps(memories, indent=2)
    print("📌 Retrieved Memories:\n", memories_str)

    return memories_str


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Step 1: Add memory (run once or keep for testing)
    add_memory()

    # Step 2: Retrieve memory
    get_memory_by_query()
