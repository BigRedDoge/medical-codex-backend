-- Create Languages table
CREATE TABLE Languages (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    code VARCHAR(10) UNIQUE
);

-- Create Source table
CREATE TABLE Source (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    quality INTEGER
);

-- Create Words table
CREATE TABLE Words (
    id INTEGER PRIMARY KEY,
    word VARCHAR(255) UNIQUE,
    language_id INTEGER,
    source_id INTEGER,
    FOREIGN KEY (language_id) REFERENCES Languages(id),
    FOREIGN KEY (source_id) REFERENCES Source(id)
);

-- Create Translations table
CREATE TABLE Translations (
    id INTEGER PRIMARY KEY,
    word1_id INTEGER,
    word2_id INTEGER,
    source_id INTEGER,
    FOREIGN KEY (word1_id) REFERENCES Words(id),
    FOREIGN KEY (word2_id) REFERENCES Words(id),
    FOREIGN KEY (source_id) REFERENCES Source(id)
);

-- Create TypeNormalizedIdentifiers table
CREATE TABLE TypeNormalizedIdentifiers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

-- Create NormalizedIdentifiers table
CREATE TABLE NormalizedIdentifiers (
    id INTEGER PRIMARY KEY,
    word_id INTEGER,
    type_normalized_identifiers_id INTEGER,
    normalized_id VARCHAR(255) UNIQUE,
    FOREIGN KEY (word_id) REFERENCES Words(id),
    FOREIGN KEY (type_normalized_identifiers_id) REFERENCES TypeNormalizedIdentifiers(id)
);

-- Create indexes for foreign keys to improve query performance
CREATE INDEX idx_words_language_id ON Words(language_id);
CREATE INDEX idx_words_source_id ON Words(source_id);
CREATE INDEX idx_translations_word1_id ON Translations(word1_id);
CREATE INDEX idx_translations_word2_id ON Translations(word2_id);
CREATE INDEX idx_translations_source_id ON Translations(source_id);
CREATE INDEX idx_normalized_identifiers_word_id ON NormalizedIdentifiers(word_id);
CREATE INDEX idx_normalized_identifiers_type_id ON NormalizedIdentifiers(type_normalized_identifiers_id);