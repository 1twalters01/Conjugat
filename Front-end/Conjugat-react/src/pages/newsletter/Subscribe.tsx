import { useState } from "react"
import LoadSubscribeForm from "../../components/newsletter/subscribe/LoadSubscribeForm";

function Subscribe() {
  const [loading, setLoading] = useState(true);
  const [done, setDone] = useState(false)
  if (done == false) {
    return (
      <div>
        <h1>Subscribe</h1>

        <LoadSubscribeForm
          loading={loading}
          setDone={setDone}
          setLoading={setLoading}
        />
      </div>
    )
  }
  return (
    <p>Sign up successful</p>
  )
}



export default Subscribe