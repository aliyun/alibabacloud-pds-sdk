// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * create_share_link request
     */
    public class CreateShareLinkRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// addition_data
        /// </summary>
        [NameInMap("addition_data")]
        [Validation(Required=false)]
        public Dictionary<string, object> AdditionData { get; set; }

        /// <summary>
        /// description
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false)]
        public string Description { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// expiration
        /// </summary>
        [NameInMap("expiration")]
        [Validation(Required=false)]
        public string Expiration { get; set; }

        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("file_id")]
        [Validation(Required=false)]
        public string FileId { get; set; }

        /// <summary>
        /// file_id_list
        /// </summary>
        [NameInMap("file_id_list")]
        [Validation(Required=false)]
        public List<string> FileIdList { get; set; }

        /// <summary>
        /// file_path_list
        /// </summary>
        [NameInMap("file_path_list")]
        [Validation(Required=false)]
        public List<string> FilePathList { get; set; }

        [NameInMap("referer")]
        [Validation(Required=false)]
        public string Referer { get; set; }

        /// <summary>
        /// share_name
        /// </summary>
        [NameInMap("share_name")]
        [Validation(Required=false)]
        public string ShareName { get; set; }

        /// <summary>
        /// share_pwd
        /// </summary>
        [NameInMap("share_pwd")]
        [Validation(Required=false)]
        public string SharePwd { get; set; }

    }

}
