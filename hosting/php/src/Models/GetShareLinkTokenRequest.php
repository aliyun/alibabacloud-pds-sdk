<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * get_share_token request
 */
class GetShareLinkTokenRequest extends Model {
    protected $_name = [
        'shareId' => 'share_id',
        'sharePwd' => 'share_pwd',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->sharePwd) {
            $res['share_pwd'] = $this->sharePwd;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetShareLinkTokenRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['share_pwd'])){
            $model->sharePwd = $map['share_pwd'];
        }
        return $model;
    }
    /**
     * @description share_id
     * @example z6e81Up4u3GDBoJ741dm8z8fZBc2dh8gW
     * @var string
     */
    public $shareId;

    /**
     * @description share_pwd
     * @example 12ABcd
     * @var string
     */
    public $sharePwd;

}
