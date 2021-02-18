<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * create_share_link response.
 */
class CreateShareLinkResponse extends Model
{
    /**
     * @description description
     *
     * @example desc
     *
     * @var string
     */
    public $description;

    /**
     * @description share_id
     *
     * @example z6e81Up4u3GDBoJ741dm8z8fZBc2dh8gW
     *
     * @var string
     */
    public $shareId;

    /**
     * @description share_msg
     *
     * @example 复制这段话¢oJ311MvRD8R¢打開阿里云宝App【来自xxx的分享】
     *
     * @var string
     */
    public $shareMsg;

    /**
     * @description share_name
     *
     * @example name
     *
     * @var string
     */
    public $shareName;

    /**
     * @description share_policy
     *
     * @example url
     *
     * @var string
     */
    public $sharePolicy;

    /**
     * @description share_pwd
     *
     * @example 12ABcd
     *
     * @var string
     */
    public $sharePwd;

    /**
     * @description share_url
     *
     * @example https://www.aliyundrive.com/sharelinks/index/abcdefghi
     *
     * @var string
     */
    public $shareUrl;
    protected $_name = [
        'description' => 'description',
        'shareId'     => 'share_id',
        'shareMsg'    => 'share_msg',
        'shareName'   => 'share_name',
        'sharePolicy' => 'share_policy',
        'sharePwd'    => 'share_pwd',
        'shareUrl'    => 'share_url',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->shareMsg) {
            $res['share_msg'] = $this->shareMsg;
        }
        if (null !== $this->shareName) {
            $res['share_name'] = $this->shareName;
        }
        if (null !== $this->sharePolicy) {
            $res['share_policy'] = $this->sharePolicy;
        }
        if (null !== $this->sharePwd) {
            $res['share_pwd'] = $this->sharePwd;
        }
        if (null !== $this->shareUrl) {
            $res['share_url'] = $this->shareUrl;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateShareLinkResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }
        if (isset($map['share_msg'])) {
            $model->shareMsg = $map['share_msg'];
        }
        if (isset($map['share_name'])) {
            $model->shareName = $map['share_name'];
        }
        if (isset($map['share_policy'])) {
            $model->sharePolicy = $map['share_policy'];
        }
        if (isset($map['share_pwd'])) {
            $model->sharePwd = $map['share_pwd'];
        }
        if (isset($map['share_url'])) {
            $model->shareUrl = $map['share_url'];
        }

        return $model;
    }
}
