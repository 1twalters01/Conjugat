import '../../sass/Components/Input fields/TotpField.scss'

function TotpField({ totp, handleTotp }: {totp:string, handleTotp:Function}) {
    return (
      <div className='totp-field'>
        <label htmlFor="totp" className="field-text">Totp</label>
        <input
          id="totp"
          type="text"
          inputMode="numeric"
          maxLength={6}
          name="totp"
          value={totp}
          onChange={(e) => handleTotp(e)}
          required={true}
        />
      </div>
    )
}
  

export default TotpField