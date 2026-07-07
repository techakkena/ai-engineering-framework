from .ai_constants import (
    AIProvider,
    ChatModels,
    EmbeddingModels,
    ImageModels,
    AudioModels,
    ReasoningModels,
    ResponseFormat,
    PromptRole,
    TokenLimits,
    VectorStores,
    FinishReasons,
    ToolTypes,
)


def main(): 

    print()

print("Audio Models")
print("----------------")
print(AudioModels.GPT_4O_TRANSCRIBE)

print()

print("Reasoning Models")
print("----------------")
print(ReasoningModels.GPT_5)

print()

print("Vector Stores")
print("----------------")
print(VectorStores.FAISS)

print()

print("Finish Reasons")
print("----------------")
print(FinishReasons.STOP)

print()

print("Tool Types")
print("----------------")
print(ToolTypes.FUNCTION)


if __name__ == "__main__":
    main()