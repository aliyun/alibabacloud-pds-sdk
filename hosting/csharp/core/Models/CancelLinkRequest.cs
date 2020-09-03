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
    public class CancelLinkRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// 待绑定的临时token，此token只能访问绑定、取消绑定接口
        /// </summary>
        [NameInMap("temporary_token")]
        [Validation(Required=true)]
        public string TemporaryToken { get; set; }

    }

}
