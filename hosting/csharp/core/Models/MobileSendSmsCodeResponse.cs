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
    public class MobileSendSmsCodeResponse : TeaModel {
        /// <summary>
        /// 短信验证码ID
        /// </summary>
        [NameInMap("sms_code_id")]
        [Validation(Required=true)]
        public string SmsCodeId { get; set; }

    }

}
