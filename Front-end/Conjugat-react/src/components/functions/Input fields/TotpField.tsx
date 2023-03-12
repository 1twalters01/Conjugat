function TotpField({ totp, handleTotp }: {totp:string, handleTotp:Function}) {
    return (
      <div className='field'>
        <label htmlFor="totp" className="field-text">Totp</label>
        <input
          id="totp"
          type="text"
          inputMode="numeric"
          name="totp"
          value={totp}
          onChange={(e) => handleTotp(e)}
          required={true}
        />
      </div>
    )
}
  

export default TotpField