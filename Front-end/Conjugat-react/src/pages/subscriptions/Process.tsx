import { useState } from "react"
import RetrieveStatus from "../../components/subscriptions/Process/RetrieveStatus"
import Authorization from '../../functions/Authorization'

function Process() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Process</h1>

      <RetrieveStatus />
    </div>
  )
}

export default Process