// constant url as exported as global constant

// base
export const BASE_URL = "http://127.0.0.1:8000"

// authentication
export const AUTH_URL = {
    LOGIN: "/auth/authenticate/",
    REGISTER: "/auth/signup/",
    REFRESH: '/auth/authenticate/refresh/',
}

export const IMAGE_URL = (src_url) => (BASE_URL + `${src_url}`)


export const BOOK_FLIGHT = (flight, seats = 1) => (
    `/user/book_flight/${flight}/1/`
)


export const USER_URL = {
    USER_PROFILE: "/user/userprofile/",
    CREATE_PROFILE: "/user/create_profile/",
    UPLOAD_IMAGE: "/user/upload_image/"
}

export const DATA_URL = {
    FULL_COUNTRIES_LIST: "https://restcountries.com/v2/all",
    AIRPORTS_LIST: "/data/airport_list/",
    AIRLINES_LIST: "/data/airline_list/",
    COUNTRIES_LIST:"/data/country_list/"
}