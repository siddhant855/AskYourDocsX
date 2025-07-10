import re
from typing import Dict, List

class ContextMiner:
    def __init__(self):
        pass
    
    def extract_entities(self, text: str) -> Dict:
        """Extract and format entities in a readable way"""
        # Simple regex-based entity extraction (replace with spaCy/transformers for better results)
        people = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', text)
        locations = re.findall(r'\b(?:Point|Island|Harbor|Bay|City|Town|Street|Avenue)\s+[A-Z][a-z]+\b|[A-Z][a-z]+\s+(?:Point|Island|Harbor|Bay|City|Town)\b', text)
        
        # Remove duplicates
        people = list(set(people))
        locations = list(set(locations))
        
        return {
            'people': people,
            'locations': locations
        }
    
    def extract_key_themes(self, text: str) -> List[str]:
        """Extract main themes from the text"""
        # Simple keyword-based theme detection
        themes = []
        
        theme_keywords = {
            'lighthouse': ['lighthouse', 'beacon', 'light', 'keeper', 'warning'],
            'maritime': ['ship', 'ocean', 'sea', 'waves', 'storm', 'rocks'],
            'solitude': ['alone', 'solitude', 'lonely', 'isolated', 'quiet'],
            'time': ['years', 'decades', 'time', 'aging', 'old'],
            'nature': ['stars', 'wind', 'weather', 'dawn', 'dusk']
        }
        
        text_lower = text.lower()
        for theme, keywords in theme_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                themes.append(theme.capitalize())
        
        return themes
    
    def run(self, text: str) -> str:
        """Generate human-readable context summary"""
        entities = self.extract_entities(text)
        themes = self.extract_key_themes(text)
        
        # Count sentences and words for basic stats
        sentences = len(re.split(r'[.!?]+', text))
        words = len(text.split())
        
        context_summary = f"""📄 **Document Context Analysis**

**Key Characters:** {', '.join(entities['people']) if entities['people'] else 'None identified'}

**Locations Mentioned:** {', '.join(entities['locations']) if entities['locations'] else 'None identified'}

**Main Themes:** {', '.join(themes) if themes else 'General content'}

**Document Stats:** {sentences} sentences, approximately {words} words

**Content Overview:** This appears to be a narrative text focusing on {themes[0].lower() if themes else 'general topics'} with {len(entities['people'])} main character(s) mentioned."""
        
        return context_summary