// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 获取文档预览地址 response
     */
    public class GetOfficePreviewUrlResponse : TeaModel {
        /// <summary>
        /// AccessToken
        /// </summary>
        [NameInMap("access_token")]
        [Validation(Required=false)]
        public string AccessToken { get; set; }

        /// <summary>
        /// preview_url
        /// </summary>
        [NameInMap("preview_url")]
        [Validation(Required=false)]
        public string PreviewUrl { get; set; }

    }

}
