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
    public class GetCaptchaRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// App ID, 当前访问的App
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

    }

}
