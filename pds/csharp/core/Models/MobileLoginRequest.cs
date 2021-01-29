// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class MobileLoginRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// App ID, 当前访问的App
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

        /// <summary>
        /// 是否自动注册用户，使用密码登录此参数不生效
        /// </summary>
        [NameInMap("auto_register")]
        [Validation(Required=false)]
        public bool? AutoRegister { get; set; }

        /// <summary>
        /// 图片验证码ID, 密码登录需要此参数
        /// </summary>
        [NameInMap("captcha_id")]
        [Validation(Required=false)]
        public string CaptchaId { get; set; }

        /// <summary>
        /// 用户输入的验证码值, 密码登录需要此参数
        /// </summary>
        [NameInMap("captcha_text")]
        [Validation(Required=false)]
        public string CaptchaText { get; set; }

        /// <summary>
        /// AES-256对称加密密钥，通过App公钥加密后传输
        /// </summary>
        [NameInMap("encrypted_key")]
        [Validation(Required=false)]
        public string EncryptedKey { get; set; }

        /// <summary>
        /// 环境参数
        /// </summary>
        [NameInMap("nvc_param")]
        [Validation(Required=true)]
        public string NvcParam { get; set; }

        /// <summary>
        /// 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
        /// </summary>
        [NameInMap("password")]
        [Validation(Required=false)]
        public string Password { get; set; }

        /// <summary>
        /// 待查询的手机号
        /// </summary>
        [NameInMap("phone_number")]
        [Validation(Required=true)]
        public string PhoneNumber { get; set; }

        /// <summary>
        /// 国家编号，默认86，不需要填+号，直接填数字
        /// </summary>
        [NameInMap("phone_region")]
        [Validation(Required=false)]
        public string PhoneRegion { get; set; }

        /// <summary>
        /// 短信验证码内容，使用密码登录此参数不生效
        /// </summary>
        [NameInMap("sms_code")]
        [Validation(Required=false)]
        public string SmsCode { get; set; }

        /// <summary>
        /// 短信验证码ID，使用密码登录此参数不生效
        /// </summary>
        [NameInMap("sms_code_id")]
        [Validation(Required=false)]
        public string SmsCodeId { get; set; }

    }

}
