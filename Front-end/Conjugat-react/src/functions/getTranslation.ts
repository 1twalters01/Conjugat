export const getTranslation = (translations: any, language: string, text: string) => {
    return translations[language][text];
}