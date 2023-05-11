export const getTranslation = (translations: any, language: string, text: string) => {
    return translations[language][text];
}

export const getTranslationList = (translations: any, language: string) => {
    return translations[language];
}