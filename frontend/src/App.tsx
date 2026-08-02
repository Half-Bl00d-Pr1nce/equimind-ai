import { APP_NAME, APP_VERSION } from "./utils/constants";

function App() {
  return (
    <div>
      <h1>{APP_NAME}</h1>
      <p>Version {APP_VERSION}</p>
    </div>
  );
}

export default App;