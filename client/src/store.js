import { applyMiddleware, } from 'redux';
import { configureStore } from '@reduxjs/toolkit';
import reduxThunk from 'redux-thunk';
import rootReducer from './reducers';
import { composeWithDevTools } from '@redux-devtools/extension';
const initialState = {};

const middleware = [reduxThunk];

const store = configureStore({
    reducer: rootReducer,
    initialState,
    // middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
    devTools: composeWithDevTools(applyMiddleware(...middleware)),
    });

export default store;