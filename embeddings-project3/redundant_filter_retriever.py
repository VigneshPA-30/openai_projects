from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma
from langchain.schema import BaseRetriever


class RedundantFilterRetriever(BaseRetriever):
        embeddings:Embeddings
        chroma:Chroma

    def get_relevant_documents(self,query):
        emb = self.embeddings.embed_query(query)

        results = self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lamba_mult=0.8
        )

        return results

    async def get_relevant_documents():
        return []