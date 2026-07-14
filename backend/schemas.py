from typing import Literal, Optional

from pydantic import BaseModel, Field


class HistoryMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)
    history: list[HistoryMessage] = Field(default_factory=list)


class Source(BaseModel):
    source: str
    chunk_index: int
    preview: str
    content: str = ""
    confidence: int = Field(..., ge=0, le=100, description="0-100 confidence score")
    confidence_label: str = "Weak Match"
    distance: float
    heading: Optional[str] = None
    retrieval: Optional[str] = None  # dense | bm25 | hybrid
    matched_terms: list[str] = Field(default_factory=list)
    matched_sentence: str = ""
    relevant_paragraph: str = ""
    citation_id: int = 1


class TimingBreakdown(BaseModel):
    embedding_sec: float = 0.0
    retrieval_sec: float = 0.0
    prompt_sec: float = 0.0
    llm_sec: float = 0.0
    total_sec: float = 0.0


class GenerationMeta(BaseModel):
    retrieved_chunks: int
    embedding_model: str
    llm: str
    generation_time_sec: float  # alias of total for compatibility
    retrieval_mode: str = "hybrid"
    timings: TimingBreakdown = Field(default_factory=TimingBreakdown)


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]
    meta: GenerationMeta
    suggestions: list[str] = Field(default_factory=list)
    flow_steps: list[str] = Field(default_factory=list)


class UploadResponse(BaseModel):
    filename: str
    chunks_indexed: int
    message: str


class DocumentInfo(BaseModel):
    source: str
    chunk_count: int
    status: str = "Indexed"
    last_indexed: Optional[str] = None


class DocumentListResponse(BaseModel):
    documents: list[DocumentInfo]
    total_documents: int = 0
    total_chunks: int = 0
    embedding_model: str = ""


class HealthResponse(BaseModel):
    status: str
    model: str
    database: str
    embedding_model: str
