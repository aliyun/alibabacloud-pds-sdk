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
    public class Captcha : TeaModel {
        /// <summary>
        /// 图片验证码，base64格式
        /// </summary>
        [NameInMap("captcha")]
        [Validation(Required=true)]
        public string Captcha_ { get; set; }

        /// <summary>
        /// 图片格式
        /// </summary>
        [NameInMap("captcha_format")]
        [Validation(Required=true)]
        public string CaptchaFormat { get; set; }

        /// <summary>
        /// 图片验证码ID
        /// </summary>
        [NameInMap("captcha_id")]
        [Validation(Required=true)]
        public string CaptchaId { get; set; }

    }

}
