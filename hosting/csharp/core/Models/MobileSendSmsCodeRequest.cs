// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class MobileSendSmsCodeRequest : TeaModel {
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
        /// 图片验证码ID
        /// </summary>
        [NameInMap("captcha_id")]
        [Validation(Required=false)]
        public string CaptchaId { get; set; }

        /// <summary>
        /// 用户输入的验证码值
        /// </summary>
        [NameInMap("captcha_text")]
        [Validation(Required=false)]
        public string CaptchaText { get; set; }

        /// <summary>
        /// 待发送验证短信的手机号
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
        /// 验证码用途, 可下发: login、register、change_password
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

    }

}
