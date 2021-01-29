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
    public class MobileRegisterRequest : TeaModel {
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
        /// 环境参数
        /// </summary>
        [NameInMap("nvc_param")]
        [Validation(Required=true)]
        public string NvcParam { get; set; }

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
        /// 短信验证码内容
        /// </summary>
        [NameInMap("sms_code")]
        [Validation(Required=true)]
        public string SmsCode { get; set; }

        /// <summary>
        /// 短信验证码ID
        /// </summary>
        [NameInMap("sms_code_id")]
        [Validation(Required=true)]
        public string SmsCodeId { get; set; }

    }

}
