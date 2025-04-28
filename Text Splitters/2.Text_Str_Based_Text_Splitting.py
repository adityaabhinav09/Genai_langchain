## Recursive based chuncking works as it first tried to find paragraph change if found then will split it based upon that if not then it will find lines and split upon that if that also not found then will split upon words and then on characters.

from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """ Space exploration has led to incredible scientific discoveris. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what's possible beyong our
planet.
These missions have not only expanded our knowledge of the universe but have also contributed to advancement in technology here on Earth. Satellite communications, GPS, and even certain
medical imaging techniques trace their roots back to innovations driven by space programs.
"""

splitters = RecursiveCharacterTextSplitter(
    chunk_size = 130,
    chunk_overlap = 0,

)

result = splitters.split_text(text)

print(result[0])
