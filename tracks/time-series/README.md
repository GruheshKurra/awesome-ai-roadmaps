# Time Series

Goal: Learn forecasting for ordered observations, from stationarity and classical baselines through deep sequence models, attention-based multi-horizon forecasters, and simple linear checks on transformer claims.

Prereqs: [ML Basics](../ml-basics/). [Deep Learning](../deep-learning/) helps for the neural forecasting papers. The simple forecasting chapter uses R; its equations can also be followed without running the code.

Status: done

Choose time-ordered evaluation splits before fitting models. Compare forecasts against naïve and seasonal-naïve baselines at the same forecast horizon before trying more complex methods. Bold links open YouTube.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Why ordered data needs special care | **[Why Are Time Series Special?](https://www.youtube.com/watch?v=ZoJ2OctrFLA)** | [Darts — Overview of forecasting models](https://unit8co.github.io/darts/userguide/forecasting_overview.html) |
| 2 | Stationarity | **[Time Series Talk — Stationarity](https://www.youtube.com/watch?v=oY-j2Wof51c)** | [Wikipedia — Stationary process](https://en.wikipedia.org/wiki/Stationary_process) |
| 3 | Autocorrelation and partial autocorrelation | **[Time Series Talk — Autocorrelation and Partial Autocorrelation](https://www.youtube.com/watch?v=DeORzP0go5I)** | [Wikipedia — Autocorrelation](https://en.wikipedia.org/wiki/Autocorrelation) |
| 4 | Time-aware evaluation splits | **[Evaluating Time Series Models](https://www.youtube.com/watch?v=kgBDQ3baESw)** | [scikit-learn — TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) |
| 5 | Mean, naïve, seasonal-naïve, and drift baselines | | [Hyndman & Athanasopoulos — Some simple forecasting methods](https://otexts.com/fpp3/simple-methods.html) |
| 6 | ARIMA | **[Time Series Talk — ARIMA Model](https://www.youtube.com/watch?v=3UmyHed0iYE)** | [statsmodels — Autoregressive Integrated Moving Average (ARIMA) Tutorial](https://www.statsmodels.org/stable/examples/notebooks/generated/autoregressive_integrated_moving_average.html) |
| 7 | Exponential smoothing | **[What are Exponential Smoothing Models](https://www.youtube.com/watch?v=hAD5vVz07ZA)** | [statsmodels — Exponential smoothing](https://www.statsmodels.org/stable/examples/notebooks/generated/exponential_smoothing.html) |
| 8 | LSTM sequence forecasting | **[Time Series Forecasting With RNN (LSTM)](https://www.youtube.com/watch?v=S8tpSG6Q2H0)** | [Christopher Olah — Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) |
| 9 | DeepAR probabilistic forecasting | **[DeepAR — Probabilistic forecasting with autoregressive recurrent networks](https://www.youtube.com/watch?v=PyGuOa9YX1k)** | [Salinas et al. 2017 — DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks](https://arxiv.org/abs/1704.04110) |
| 10 | N-BEATS basis expansion | **[N-BEATS: Neural basis expansion analysis for interpretable time series forecasting](https://www.youtube.com/watch?v=r4i8bY_-dvM)** | [Oreshkin et al. 2019 — N-BEATS](https://arxiv.org/abs/1905.10437) |
| 11 | Temporal Fusion Transformer | **[Temporal Fusion Transformers, EXPLAINED](https://www.youtube.com/watch?v=V14qoa5vZ1I)** | [Lim et al. 2019 — Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting](https://arxiv.org/abs/1912.09363) |
| 12 | Informer for long sequences | **[Informer: Time series Transformer — EXPLAINED](https://www.youtube.com/watch?v=aETHYkoJeNY)** | [Zhou et al. 2020 — Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting](https://arxiv.org/abs/2012.07436) |
| 13 | Linear baselines vs transformers | **[LTSF-Linear: Are Transformers Effective for Time Series Forecasting](https://www.youtube.com/watch?v=Su2Bj37rAFs)** | [Zeng et al. 2022 — Are Transformers Effective for Time Series Forecasting?](https://arxiv.org/abs/2205.13504) |
| 14 | PatchTST patching | **[How PatchTST and Chronos differ for Time Series Forecasting](https://www.youtube.com/watch?v=8LD_OiTxtwQ)** | [Nie et al. 2022 — A Time Series is Worth 64 Words: Long-term Forecasting with Transformers](https://arxiv.org/abs/2211.14730) |
