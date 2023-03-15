import { useState } from "react"
import LoadUnsubscribeForm from "../../components/newsletter/subscribe/LoadUnsubscribeform"

function Unsubscribe() {
  const [loading, setLoading] = useState(true);
  const [done, setDone] = useState(false)
  if (done == false) {
    return (
      <div>
        <h1>Subscribe</h1>

        <LoadUnsubscribeForm
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

export default Unsubscribe