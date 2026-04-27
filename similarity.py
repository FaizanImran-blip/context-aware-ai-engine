
json_key_list_with_semantics = [

    {"key": "metadata.version", "polarity": "neutral", "context": "structure_info", "keywords": ["version", "json version"]},
    {"key": "metadata.author", "polarity": "positive", "context": "self_identity", "keywords": ["faizan", "author", "created by"]},
    {"key": "metadata.type", "polarity": "neutral", "context": "data_type", "keywords": ["knowledge graph", "personal db"]},
    

    {"key": "entities.person.faizan.id", "polarity": "neutral", "context": "identifier", "keywords": ["faizan id"]},
    {"key": "entities.person.faizan.name", "polarity": "positive", "context": "self", "keywords": ["my name", "faizan"]},
    {"key": "entities.person.faizan.role", "polarity": "positive", "context": "career", "keywords": ["ai engineer", "senior ai engineer", "fullstack developer"]},
    {"key": "entities.person.faizan.personality_traits", "polarity": "positive", "context": "character", "keywords": ["hardworking", "smart", "emotional", "respectful"]},
    {"key": "entities.person.faizan.current_semester", "polarity": "neutral", "context": "education", "keywords": ["semester", "3rd semester"]},
    {"key": "entities.person.faizan.education.university", "polarity": "negative", "context": "education", "keywords": ["university", "UMT", "which university"]},
    {"key": "entities.person.faizan.education.department", "polarity": "positive", "context": "education", "keywords": ["AI department", "CS department"]},
    {"key": "entities.person.faizan.education.criticism", "polarity": "negative", "context": "complaint", "keywords": ["teachers discouraged ai", "cgpa pressure", "grade chasing"]},
    
    # FAMILY
    {"key": "entities.person.faizan.family.parents.support_level", "polarity": "positive", "context": "family_support", "keywords": ["parents support", "mom dad support"]},
    {"key": "entities.person.faizan.family.siblings.sisters", "polarity": "positive", "context": "family", "keywords": ["sisters", "three sisters", "behne"]},
    {"key": "entities.person.faizan.family.siblings.only_brother", "polarity": "neutral", "context": "family_role", "keywords": ["only brother", "ek bhai"]},
    
    # LOVE INTEREST
    {"key": "entities.person.faizan.love_interest.status", "polarity": "negative", "context": "romance", "keywords": ["unrequited love", "one sided love"]},
    {"key": "entities.person.love_interest_girl.id", "polarity": "neutral", "context": "other_person", "keywords": ["girl id", "she"]},
    {"key": "entities.person.love_interest_girl.department", "polarity": "neutral", "context": "other_person", "keywords": ["cs girl", "her department"]},
    {"key": "entities.person.love_interest_girl.first_sight", "polarity": "positive", "context": "memory", "keywords": ["first sight", "orientation day", "pehli nazar"]},
    {"key": "entities.person.love_interest_girl.current_status", "polarity": "negative", "context": "rejection", "keywords": ["refuses contact", "doesn't talk"]},
    {"key": "entities.person.love_interest_girl.filed_complaint", "polarity": "negative", "context": "legal", "keywords": ["harassment complaint", "case", "security office"]},
    {"key": "entities.person.love_interest_girl.observed_actions", "polarity": "mixed", "context": "behavior", "keywords": ["smiled", "angry", "ignores", "looks from door"]},
    
    # INCIDENTS
    {"key": "entities.incident.harassment_complaint.id", "polarity": "negative", "context": "legal", "keywords": ["complaint id", "inc001"]},
    {"key": "entities.incident.harassment_complaint.faizan_response", "polarity": "positive", "context": "honesty", "keywords": ["told truth", "full truth"]},
    {"key": "entities.incident.harassment_complaint.faizan_emotional_state", "polarity": "negative", "context": "emotion", "keywords": ["crying", "heartbroken", "roya"]},
    {"key": "entities.incident.harassment_complaint.potential_consequence", "polarity": "negative", "context": "risk", "keywords": ["expulsion", "remove from university"]},
    
    {"key": "entities.incident.interaction_attempts.timeline", "polarity": "mixed", "context": "story_sequence", "keywords": ["orientation", "sem1", "sem2", "sem3", "followed", "lift", "email"]},
    
    # UNIVERSITY
    {"key": "entities.university.UMT.full_name", "polarity": "neutral", "context": "organization", "keywords": ["UMT", "university full name"]},
    {"key": "entities.university.UMT.faizan_view", "polarity": "negative", "context": "criticism", "keywords": ["gave nothing", "university ne kuch nahi dia"]},
    {"key": "entities.university.UMT.teaching_style", "polarity": "negative", "context": "hypocrisy", "keywords": ["discourages ai", "teachers use ai", "hypocrisy"]},
    {"key": "entities.university.UMT.focus", "polarity": "negative", "context": "education_system", "keywords": ["cgpa focus", "grades only", "no practical"]},
    
    # SKILLS
    {"key": "entities.skill_domain.faizan_skills.ai_engineering", "polarity": "positive", "context": "expertise", "keywords": ["ai expert", "senior ai"]},
    {"key": "entities.skill_domain.faizan_skills.fullstack_dev", "polarity": "positive", "context": "expertise", "keywords": ["fullstack", "frontend backend"]},
    
    # RELATIONS
    {"key": "relations.links", "polarity": "mixed", "context": "connections", "keywords": ["relationship", "graph", "links"]},
    {"key": "relations.links.loves", "polarity": "positive", "context": "feeling", "keywords": ["loves her", "pyar", "like"]},
    {"key": "relations.links.fears", "polarity": "negative", "context": "anxiety", "keywords": ["fear", "dar", "uncomfortable"]},
    {"key": "relations.links.files_complaint_against", "polarity": "negative", "context": "conflict", "keywords": ["complaint filed", "shikayat"]},
    {"key": "relations.links.dislikes", "polarity": "negative", "context": "opinion", "keywords": ["dislikes university", "pasand nahi"]},
    {"key": "relations.links.supported_by", "polarity": "positive", "context": "support", "keywords": ["parents support", "family support"]},
    
    # SEMANTIC CLUSTERS
    {"key": "semantic_graph.clusters.emotional_conflict", "polarity": "negative", "context": "emotional", "keywords": ["love fear", "heartbreak", "guilt", "longing"]},
    {"key": "semantic_graph.clusters.professional_identity", "polarity": "positive", "context": "career", "keywords": ["senior ai", "smart worker"]},
    {"key": "semantic_graph.clusters.family_backbone", "polarity": "positive", "context": "family", "keywords": ["family support", "sisters", "parents belief"]},
    {"key": "semantic_graph.clusters.university_failure", "polarity": "negative", "context": "criticism", "keywords": ["anti ai", "no value", "cgpa system"]},
    
    # VECTOR CHUNKS
    {"key": "vector_search_ready.chunks.chunk1", "polarity": "positive", "context": "summary", "keywords": ["senior ai", "3rd semester", "smart"]},
    {"key": "vector_search_ready.chunks.chunk2", "polarity": "negative", "context": "love_story", "keywords": ["fell in love", "complaint", "cried"]},
    {"key": "vector_search_ready.chunks.chunk3", "polarity": "negative", "context": "university", "keywords": ["teachers discouraged ai", "cgpa", "no value"]},
    {"key": "vector_search_ready.chunks.chunk4", "polarity": "mixed", "context": "timeline", "keywords": ["orientation", "smile", "ignores", "still likes"]},
    {"key": "vector_search_ready.chunks.chunk5", "polarity": "negative", "context": "legal", "keywords": ["harassment complaint", "security officer", "expulsion"]},
    
    # QUERY EXAMPLES
    {"key": "query_examples.semantic_questions", "polarity": "neutral", "context": "examples", "keywords": ["example questions"]},
]

# Helper function to detect polarity of a user query
def detect_query_polarity(user_query):
    """
    Returns 'positive', 'negative', 'mixed', or 'neutral'
    based on matching keywords in the query.
    """
    user_query_lower = user_query.lower()
    positive_keywords = ["love", "support", "smart", "hardworking", "success", "good", "best", "achieve", "proud"]
    negative_keywords = ["complaint", "harassment", "crying", "heartbreak", "fail", "hypocrisy", "no value", "expel", "remove", "angry", "ignore"]
    
    pos_score = sum(1 for kw in positive_keywords if kw in user_query_lower)
    neg_score = sum(1 for kw in negative_keywords if kw in user_query_lower)
    
    if pos_score > 0 and neg_score == 0:
        return "positive"
    elif neg_score > 0 and pos_score == 0:
        return "negative"
    elif pos_score > 0 and neg_score > 0:
        return "mixed"
    else:
        return "neutral"

