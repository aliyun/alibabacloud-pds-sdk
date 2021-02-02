// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 获取视频DRM License
     */
    public class HostingVideoDRMLicenseRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// drmType
        /// </summary>
        [NameInMap("drmType")]
        [Validation(Required=true)]
        public string DrmType { get; set; }

        /// <summary>
        /// licenseRequest
        /// </summary>
        [NameInMap("licenseRequest")]
        [Validation(Required=true)]
        public string LicenseRequest { get; set; }

    }

}
